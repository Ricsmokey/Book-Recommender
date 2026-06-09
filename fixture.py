import requests
html = requests.get("https://books.toscrape.com/catalogue/page-1.html").text
with open("listing_page.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Fixture saved.")