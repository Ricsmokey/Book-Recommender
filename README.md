# Books to Scrape — Scraper & Django Explorer

A full-stack Python project: a web scraper that collects all 1,000 books from
[books.toscrape.com](https://books.toscrape.com) stores them into a SQLite database and a
Django web app that displays a random book — cover, rating, price, and
description — on a clean, responsive page.

## Live demo
https://book-recommender-lun2.onrender.com

## Features
- Pagination across all 50 catalogue pages
- Two-layer scraping: listing data plus each book's detail page (category, description)
- SQLite storage with deduplication on the book URL
- Unit tests for the parser, run offline against a saved HTML fixture
- Django app that serves a random book in a styled card
- Deployed on Render

## Tech stack
* Python
* requests
* BeautifulSoup
* SQLite
* pytest
* Django
* gunicorn
* WhiteNoise
* Render

## Project structure

Book-Recommender/
│
├── books/
├── bookshelf/
├── scraper.py
├── test_scraper.py
├── fixture.py
├── listing_page.html
├── manage.py
├── db.sqlite3
└── requirements.txt


## Run locally
The database ships with the repo, so you can run the web app straight away:

pip install -r requirements.txt
python manage.py runserver
## open http://127.0.0.1:8000/


## Testing Case

python -m pytest

## **Author**
Akorede Kareem — github.com/Ricsmokey

