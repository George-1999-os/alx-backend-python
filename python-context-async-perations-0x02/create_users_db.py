import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
    )
''')

# Insert some test data
cursor.executemany('''
    INSERT INTO users (name, email, age)
    VALUES (?, ?, ?)
''', [
    ("Alice", "alice@example.com", 30),
    ("Bob", "bob@example.com", 20),
    ("Charlie", "charlie@example.com", 28),
])

conn.commit()
conn.close()
