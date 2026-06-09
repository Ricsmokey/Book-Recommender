import sqlite3
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

URL = "https://books.toscrape.com/catalogue/page-1.html"
DB_NAME = "Books.db"
RATING_MAP = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}


def setup_database(db_name=DB_NAME):
    # Create the database
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS books')
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT,
        availability TEXT,
        rating INTEGER,
        book_url TEXT UNIQUE,
        image_url TEXT,
        category TEXT,
        description TEXT
    )''')
    connection.commit()      
    return connection         


def parse_listing_page(soup, page_url):
    # Parse the HTML
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        books.append({
            'title': book.h3.a['title'],
            'price': book.find('p', class_='price_color').text.strip(),
            'availability': book.find('p', class_='instock availability').text.strip(),
            'rating': RATING_MAP[book.find('p', class_='star-rating')['class'][1]],
            'book_url': urljoin(page_url, book.h3.a['href']),
            'image_url': urljoin(page_url, book.find('img')['src']),
        })
    return books


def get_book_details(book_url):
    # Getting the book details page and returning the category & description
    response = requests.get(book_url, timeout=10)
    response.encoding = 'utf-8'
    try:
        response.raise_for_status()
    except Exception as e:
        print(f"Book page not found - skipping gracefully: {e}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    description_div = soup.find('div', id='product_description')
    description = description_div.find_next_sibling('p').text.strip() if description_div else 'No description available'
    category = soup.find('ul', class_='breadcrumb').find_all('li')[2].a.text.strip()
    return {'category': category, 'description': description}


def scrape_all_books(start_url=URL):
    # Looping through all the pages
    rows = []
    url = start_url
    page_count = 0
    while url:
        response = requests.get(url, timeout=10)
        response.encoding = 'utf-8'
        try:
            response.raise_for_status()
        except Exception as e:
            print(f"Page not found - skipping gracefully: {e}")
            break
        soup = BeautifulSoup(response.text, 'html.parser')

        for book in parse_listing_page(soup, url):        # the small parser does its one job
            details = get_book_details(book['book_url'])
            if details is None:
                continue
            rows.append((book['title'], book['price'], book['availability'], book['rating'],
                         book['book_url'], book['image_url'],
                         details['category'], details['description']))
            time.sleep(0.3)

        next_page = soup.find('li', class_='next')
        url = urljoin(url, next_page.a['href']) if next_page else None
        page_count += 1
        print(f"Pages done: {page_count} | books collected: {len(rows)}")
    return rows


def save_books(connection, rows):
    # Inserting all the books into the database
    cursor = connection.cursor()
    cursor.executemany('''INSERT OR IGNORE INTO books
        (title, price, availability, rating, book_url, image_url, category, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', rows)
    connection.commit()


def main():
    connection = setup_database()
    rows = scrape_all_books()
    save_books(connection, rows)
    connection.close()
    print(f"Stored {len(rows)} books.")


if __name__ == "__main__":
    main()