# Website Copy Analyzer

![Website Copy Analyzer Screenshot](https://github.com/andresolerc/website-copy-analyzer/raw/main/website-copy-analyser.png)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation & Usage](#installation--usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

Website Copy Analyzer is a state-of-the-art tool designed to empower marketers, copywriters, and website owners by providing insightful analysis of website copy. Leveraging the advanced capabilities of OpenAI's GPT-4, this application not only scrapes website content but also offers recommendations to optimize the copy for enhanced engagement and conversion.

## Features

- **Comprehensive Scraping**: Extracts various elements including headlines, paragraphs, list items, anchor tags, image alt texts, meta descriptions, and emphasized text from websites.
- **In-depth Analysis**: Utilizes the cutting-edge OpenAI's GPT-4 for detailed and insightful analysis of the scraped content.
- **User-Friendly Interface**: Features a Streamlit-based interface for effortless input and clear, intuitive presentation of analysis results.
- **Exportable Results**: Offers the functionality to download the comprehensive analysis report in CSV format for further use.

## Prerequisites

- Python 3.8 or higher
- Pip (Python package manager)
- OpenAI API key

## Installation & Usage

1. **Clone the Repository**
   ```sh
   git clone https://github.com/andresolerc/website-copy-analyzer.git
   cd website-copy-analyzer

2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt

3. **Run the Application**
   ```sh
   streamlit run app.py

4. Open in Browser
    Navigate to http://localhost:8501 in your web browser.
5. Enter Website URL & API Key
    Input the URL of the website you wish to analyze and your OpenAI API key in the respective fields.
6. View & Download Analysis
    Explore the analysis results displayed on the interface and download the report as needed.

## Configuration

The application can be configured by modifying the app.py file (if available) or by setting environment variables. Refer to the application documentation for a list of available configuration options.

## Contributing
We welcome contributions from the community! For details on how to contribute, please read our ![Contributing Guidelines](https://chat.openai.com/c/CONTRIBUTING.md). Adherence to our ![Code of Conduct](https://chat.openai.com/c/CODE_OF_CONDUCT.md) is expected.

## Support
If you encounter any issues or require further assistance, please raise an issue on the GitHub repository, and we will address it promptly.

## License
This project is licensed under the MIT License. See the ![LICENSE](https://chat.openai.com/c/LICENSE) file for more information.

## Acknowledgements
![OpenAI](https://www.openai.com/) for the incredible GPT-4 API.
![Streamlit](https://streamlit.io/) for providing an amazing web application framework.
![Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for enabling efficient HTML scraping.

