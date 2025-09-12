import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create 'users' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insert sample data
cursor.execute("INSERT INTO users (id, name, email) VALUES (1, 'Alice', 'alice@example.com')")
cursor.execute("INSERT INTO users (id, name, email) VALUES (2, 'Bob', 'bob@example.com')")

conn.commit()
conn.close()

print("users.db and table created successfully.")
