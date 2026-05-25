# =====================================================
# CODEALPHA WEB SCRAPING PROJECT
# QUOTES WEBSITE SCRAPER
# =====================================================

# IMPORT LIBRARIES

import requests
from bs4 import BeautifulSoup
import pandas as pd

# =====================================================
# WEBSITE URL
# =====================================================

url = "https://quotes.toscrape.com"

# SEND REQUEST

response = requests.get(url)

# PARSE HTML

soup = BeautifulSoup(response.text, "html.parser")

# =====================================================
# EXTRACT QUOTES
# =====================================================

quotes_data = []

quotes = soup.find_all("div", class_="quote")

for quote in quotes:

    text = quote.find("span", class_="text").text

    author = quote.find("small", class_="author").text

    tags = [tag.text for tag in quote.find_all("a", class_="tag")]

    quotes_data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })

# =====================================================
# CREATE DATAFRAME
# =====================================================

df = pd.DataFrame(quotes_data)

# =====================================================
# DISPLAY DATA
# =====================================================

print("\n SCRAPED DATA\n")

print(df)

# =====================================================
# SAVE TO CSV
# =====================================================

df.to_csv("quotes_data.csv", index=False)

print("\n DATA SAVED TO quotes_data.csv")

print("\n WEB SCRAPING PROJECT COMPLETED")