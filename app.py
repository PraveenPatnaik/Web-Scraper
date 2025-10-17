import streamlit as st
import pandas as pd
from scraper import scrape_data

st.set_page_config(page_title="Generic Web Scraper", layout="wide")
st.title("🌐 Generic Web Scraper App")

url = st.text_input("Enter the URL to scrape:", "")

if url:
    with st.spinner("Scraping in progress..."):
        df, message = scrape_data(url)

    if df is not None:
        st.success(message)
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download as CSV", csv, "scraped_data.csv", "text/csv")
    else:
        st.error(message)

st.markdown("---")
st.markdown("👨‍💻 Built with Streamlit + BeautifulSoup + Pandas")
