import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def clean_text(text):
    return re.sub(r'\\s+', ' ', text).strip()

def scrape_data(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return None, f"Failed to fetch the page. Status code: {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')

        tables = soup.find_all('table')
        if tables:
            df = pd.read_html(str(tables[0]))[0]
            return df, "Table data scraped successfully!"

        elements = soup.find_all(['li', 'p', 'div'])
        data = [clean_text(elem.get_text()) for elem in elements if clean_text(elem.get_text())]

        if not data:
            return None, "No meaningful data found."

        df = pd.DataFrame(data, columns=["Extracted Text"])
        return df, "Structured text data scraped successfully!"

    except Exception as e:
        return None, f"Error occurred: {str(e)}"
