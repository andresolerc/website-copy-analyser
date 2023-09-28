# Import required libraries
import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd
import openai
import csv
from concurrent.futures import ThreadPoolExecutor


# Function to scrape and categorize website content
def scrape_and_categorize_website(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Initialize empty list to store results
        results = []

        # Find headings
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            headings = soup.find_all(tag)
            for heading in headings:
                results.append({'Category': 'Heading', 'Content': heading.get_text(strip=True)})
        
        # Find paragraphs
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            results.append({'Category': 'Paragraph', 'Content': paragraph.get_text(strip=True)})
        
        # Find list items
        list_items = soup.find_all('li')
        for item in list_items:
            results.append({'Category': 'List Item', 'Content': item.get_text(strip=True)})
        
        # Find anchor tags
        anchor_tags = soup.find_all('a')
        for tag in anchor_tags:
            results.append({'Category': 'Anchor Tag', 'Content': tag.get_text(strip=True)})
        
        # Find image alt text
        images = soup.find_all('img', alt=True)
        for img in images:
            results.append({'Category': 'Image Alt Text', 'Content': img['alt']})
        
        # Find meta description
        meta_description = soup.find('meta', attrs={'name': 'description'})
        if meta_description:
            results.append({'Category': 'Meta Description', 'Content': meta_description['content']})
        
        # Find bold and italic text
        for tag in ['b', 'strong', 'i', 'em']:
            texts = soup.find_all(tag)
            for text in texts:
                results.append({'Category': 'Emphasized Text', 'Content': text.get_text(strip=True)})
        
        # Find CTAs (this is a simplified example; you may need more complex logic)
        for tag in ['button', 'a']:
            ctas = soup.find_all(tag, string=['Click Here', 'Buy Now', 'Learn More', 'Subscribe'])
            for cta in ctas:
                results.append({'Category': 'CTA', 'Content': cta.get_text()})
        
        # Find testimonials (this is a simplified example; you may need more complex logic)
        testimonials = soup.find_all('blockquote')
        for testimonial in testimonials:
            results.append({'Category': 'Testimonial', 'Content': testimonial.get_text()})
        
        # Convert results to DataFrame
        df = pd.DataFrame(results)

        # Remove duplicate rows based on the 'Content' column
        df = df.drop_duplicates(subset='Content')
        
        # Save to CSV
        df.to_csv(f"{url.replace('/', '_').replace(':', '')}_scraped.csv", index=False)
        
        return df

    except Exception as e:
        return f"Error scraping website: {str(e)}"
    

# Function to analyze text with GPT-3.5 Turbo
def analyze_text(df):
    analysis_results = []

    def analyze_row(row):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Update to "gpt-4" if available
                messages=[
                    {"role": "system", "content": "You are a helpful assistant specialized in analyzing website copy."},
                    {"role": "user", "content": f"Analyze the following {row.Category}: {row.Content}"}

                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error analyzing text: {str(e)}"
    
    # Use ThreadPoolExecutor for concurrent API calls
    with ThreadPoolExecutor() as executor:
        analysis_results = list(executor.map(analyze_row, df.itertuples(index=False)))
    
    return analysis_results

# Streamlit app
st.title("Website Copy Analyzer")

# API Key Input
api_key = st.text_input("Enter your OpenAI API key:", type='password')

if api_key:
    # Initialize OpenAI API with the entered key
    openai.api_key = api_key

# URL Input
url = st.text_input("Enter the URL of the website you want to analyze:")

if url:
    # Web Scraping and Categorization
    df = scrape_and_categorize_website(url)
    if isinstance(df, str) and df == "Error scraping website":
        st.write("Error scraping website. Please check the URL and try again.")
    else:
        # Text Analysis with GPT-3.5 Turbo
        df['Analysis'] = analyze_text(df)
        
        # Display the categorized text and analysis in a table
        st.write("Categorized Text and Analysis:")
        st.write(df)
        
        # Generate a downloadable report
        st.download_button(
            label="Download Report",
            data=df.to_csv(index=False),
            file_name="website_analysis_report.csv",
            mime="text/csv"
        )
