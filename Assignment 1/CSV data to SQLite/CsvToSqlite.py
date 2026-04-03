import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Creating table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
)
""")

# Read CSV file and insert data
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  

    for row in reader:
        name, email = row
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )

# commit the changes
conn.commit()

# Fetch and display data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows[:10]:  # show first 10 only
    print(row)

print("\nTotal Records Inserted:", len(rows))

conn.close()