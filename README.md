
# Books to Scrape — Web Scraper

A Python scraper that collects all 1,000 books from [books.toscrape.com](https://books.toscrape.com),
with their details from its own page, and store in a SQLite database.

## Features

- **Pagination** 
- **Two-layer scraping** 
- **SQLite storage** 
- **Deduplication** 
- **Tested** 

## Tech stack

Python  · requests · BeautifulSoup · sqlite3 · pytest

## Project structure

\`\`\`
Portfolio/
├── scraper.py          # main scraper: functions + main()
├── test_scraper.py     # pytest tests for the parser
├── listing_page.html   # saved HTML fixture for the tests
├── requirements.txt
└── README.md
\`\`\`

