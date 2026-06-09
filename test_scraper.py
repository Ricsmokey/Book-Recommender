from bs4 import BeautifulSoup
from scraper import parse_listing_page

PAGE_URL = "https://books.toscrape.com/catalogue/page-1.html"


def load_soup():
    with open("listing_page.html", encoding="utf-8") as f:
        return BeautifulSoup(f.read(), "html.parser")


def test_returns_twenty_books():
    books = parse_listing_page(load_soup(), PAGE_URL)
    assert len(books) == 20


def test_first_book_has_clean_fields():
    books = parse_listing_page(load_soup(), PAGE_URL)
    first = books[0]
    assert first["title"]                          # title isn't empty
    assert first["rating"] in [1, 2, 3, 4, 5]      # rating converted to an int
    assert first["book_url"].startswith("https://books.toscrape.com/catalogue/")