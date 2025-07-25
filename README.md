# python-web-scraper
This project is a simple Python web scraper that collects book data from [books.toscrape.com](https://books.toscrape.com).  
It goes through multiple pages and saves the data into a CSV file.

## 🔧 Features
- Gets book title, price, rating, and product link
- Works with pagination
- Exports to `books.csv`

## 🐍 Technologies Used
- Python 3
- requests
- BeautifulSoup
- pandas

## ▶️ How to Run

```bash
pip install -r requirements.txt
python scrape_books.py
