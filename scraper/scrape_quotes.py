import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Website URL
url = "https://quotes.toscrape.com/"

# Step 2: Send Request
response = requests.get(url)

# Step 3: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Extract Data
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Step 5: Store Data
data = []
for i in range(len(quotes)):
    data.append({
        "Quote": quotes[i].text,
        "Author": authors[i].text
    })

# Step 6: Create Dataset
df = pd.DataFrame(data)
df.to_csv("data/quotes.csv", index=False)

print("✅ Data scraped and saved successfully!")
