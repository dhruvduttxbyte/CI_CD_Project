import requests
from bs4 import BeautifulSoup
import json

def fetch_quotes():
    url = "https://quotes.toscrape.com/"

    # 1. Send the HTTP GET request
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 ScraperBot/1.0"})

    # 2. Check if the website responded successfully (Status Code 200)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch page: Status code {response.status_code}")

    # 3. Parse the raw HTML text
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes_list = []

    # 4. Extract specific elements using CSS selectors
    for quote in soup.select('div.quote'):
        text = quote.select_one('span.text').text
        author = quote.select_one('small.author').text
        tags = [tag.text for tag in quote.select('div.tags a.tag')]

        quotes_list.append({
            "quote": text,
            "author": author,
            "tags": tags
        })

    return quotes_list


if __name__ == "__main__":
    # This runs when executed directly
    data = fetch_quotes()
    print(json.dumps(data[:2], indent=2))  # Print first 2 results to verify