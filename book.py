import requests
from bs4 import BeautifulSoup
import pandas as pd


# So‘rov yuboriladigan URL'lar
base_url = "https://books.toscrape.com/catalogue/"
get_url = base_url + "page-1.html"

# Brauzer sifatida ko‘rinish uchun headers
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}
# Session ochamiz
session = requests.Session()

nomi, narxi, reyting, linki = [], [], [], []
n = 1
while get_url:
    response = session.get(get_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # with open('quotes.html', 'r', encoding='utf-8') as file:
    #     html = file.read()
    # soup = BeautifulSoup(html, 'html.parser')
    ol = soup.select_one('ol')
    print(f"🔄 Sahifa {n} yuklanmoqda...")
    n=n+1
    for li in ol.find_all('li'):
        nomi.append(li.select_one('h3').text)
        narxi.append(li.select_one('.price_color').text)
        reyting.append(li.find('p').get('class')[1])
        linki.append('https://books.toscrape.com/catalogue/'+li.find('a').get('href'))
    next_button = soup.select_one('li.next a')
    if next_button :
        get_url = base_url+next_button.get('href')
    else:break
    data = {
        'nomi': nomi,
        'narxi': narxi,
        'reyting': reyting,
        'linki': linki
    }

df = pd.DataFrame(data)
df.to_csv('book.csv', index=False)