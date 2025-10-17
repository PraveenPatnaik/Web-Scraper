# Web Scraper

A simple Streamlit app that scrapes any webpage for table or structured text data. Input a URL, and the app returns the content in a tabular format.

---

## 🚀 Features

- Auto-detects HTML **tables** or list items on given web pages.  
- Displays scraped data as a **preview** in the browser.  
- Allows users to **download** the scraped data as a CSV.  
- Supports structured text extraction in addition to table extraction.

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Framework:** Streamlit  
- **Web-scraping Libraries:** BeautifulSoup, Requests  
- **Others:** pandas, csv  

---

## ⚙️ Installation & Usage

1. Clone the repository:  
   ```bash
   git clone https://github.com/Jyotsna2409/Web_Scraper.git
   cd Web_Scraper
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
4. Open the browser window (URL given by Streamlit, usually localhost:8501) and enter the webpage URL to scrape.
