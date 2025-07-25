
# 📘 Python Book Scraper

This project is a simple Python web scraper that collects book information from [books.toscrape.com](https://books.toscrape.com).  
It extracts book title, price, rating, and product link from all pages and saves the data into a CSV file.

## 🔧 Features

- 🔄 Scrapes all pages using pagination
- 📚 Extracts:
  - Book title
  - Price
  - Rating
  - Product link
- 💾 Saves data into `book.csv`
- ✅ Easy to use and beginner-friendly

## 📦 Technologies Used

- Python 3
- `requests`
- `beautifulsoup4`
- `pandas`

## ▶️ How to Run

### 1. Install required packages:

```bash
pip install -r requirements.txt
```

### 2. Run the scraper:

```bash
python book.py
```

After running the script, a file named `book.csv` will be created containing the scraped data.

## 📂 Output Example

| Book Title              | Price  | Rating | Link                                                |
|------------------------|--------|--------|-----------------------------------------------------|
| A Light in the Attic   | £51.77 | Three  | https://books.toscrape.com/catalogue/a-light...     |
| Tipping the Velvet     | £53.74 | One    | https://books.toscrape.com/catalogue/tipping...     |
| Soumission             | £50.10 | One    | https://books.toscrape.com/catalogue/soumission...  |

## 📄 License

This project is licensed under the MIT License.

## 🙋 Author

Created by [Nuriddin Xojabayev](https://github.com/nuraddin86)
