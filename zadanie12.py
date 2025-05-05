import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
authors = {}
page = 1

while True:
    response = requests.get(f"{url}/page/{page}/")

        
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    
        
    for quote in quotes:
        author = quote.find('small', class_='author').text
        if author in authors:
            authors[author] += 1
        else:
            authors[author] = 1
    
    page += 1

    sorted_authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)

    print("Авторы по количеству цитат (по убыванию):")
    for author, count in sorted_authors:
        print(f"{author}: {count} цитат")