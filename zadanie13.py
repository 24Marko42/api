import requests
from bs4 import BeautifulSoup
import random

base_url = "https://quotes.toscrape.com"
quotes = []
page = 1

while True:
    response = requests.get(f"{base_url}/page/{page}/")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    page_quotes = soup.find_all('div', class_='quote')
    
    for quote in page_quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        quotes.append((text, author))
    
    page += 1

random_quotes = random.sample(quotes, min(5, len(quotes)))

print("Пять случайных цитат:")
for i, (text, author) in enumerate(random_quotes, 1):
    print(f"\n{i}. {text}")
    print(f"   — {author}")