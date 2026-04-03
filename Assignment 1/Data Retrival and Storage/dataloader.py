import requests
import sqlite3

API_URL = "https://openlibrary.org/search.json?q=python"

response = requests.get(API_URL)
data = response.json()

books = data['docs'][:10]  # select first 10 books

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

for book in books:
    title = book.get('title', 'N/A')
    author = book.get('author_name', ['Unknown'])[0]
    year = book.get('first_publish_year', 0)

    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
                   (title, author, year))

conn.commit()

cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()