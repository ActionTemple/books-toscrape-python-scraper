# Books to Scrape Scraper

A simple Python web scraper for http://books.toscrape.com that collects book data across all pages and exports the results to either **CSV** or **JSON** format.

This project was built as a practice exercise for learning **Python web scraping**, including pagination handling, HTML parsing, and exporting structured data.

---

## Features

* Scrapes all books from **books.toscrape.com**
* Automatically follows pagination until the final page
* Extracts:

  * **Title**
  * **Price**
  * **Availability**
* User can choose output format:

  * CSV
  * JSON
* Simple terminal interface using single-key input
* Clean separation of scraping, parsing, and output functions

---

## Technologies Used

* Python
* requests
* BeautifulSoup (bs4)
* csv
* json
* urllib.parse
* getch

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/books-scraper.git
cd books-scraper
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Requirements

requirements.txt

```
requests
bs4
getch
```

*(Other modules used such as csv, json, os, and urllib are part of the Python standard library.)*

---

## Usage

Run the scraper:

```
python3 scraper.py
```

You will see a menu:

```
Scraper for books.toscrape.com

1: CSV
2: JSON
3: Exit
```

Press:

* **1** → Export results to `books.csv`
* **2** → Export results to `books.json`
* **3** → Exit

The scraper will automatically process every page on the site.

---

## Example Output

### CSV

```
Title,Price,Availability
A Light in the Attic,£51.77,In stock
Tipping the Velvet,£53.74,In stock
Soumission,£50.10,In stock
```

### JSON

```
[
    {
        "title": "A Light in the Attic",
        "price": "£51.77",
        "availability": "In stock"
    },
    {
        "title": "Tipping the Velvet",
        "price": "£53.74",
        "availability": "In stock"
    }
]
```

---

## Project Purpose

This project was created as part of learning Python and web scraping fundamentals.
It focuses on:

* Sending HTTP requests
* Parsing HTML with BeautifulSoup
* Handling pagination
* Structuring scraped data
* Exporting data to multiple formats

---

## Source Website

This scraper is designed for the practice website:

http://books.toscrape.com

This site is intentionally built for learning web scraping.

---

## License

MIT License
