#!/usr/bin/python3
import mysql.connector
import csv
import uuid

# Connect to MySQL server
def connect_db():
    try:
        connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="georgE@3111"
)






        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create the database ALX_prodev
def create_database(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
        connection.commit()
        cursor.close()
        print("Database ALX_prodev created or already exists")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Connect to the ALX_prodev database
def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="georgE@3111",
    database="ALX_prodev"
)

        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Create the user_data table
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id CHAR(36) PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                age DECIMAL NOT NULL,
                UNIQUE KEY idx_user_id (user_id)
            );
        """)
        connection.commit()
        cursor.close()
        print("Table user_data created successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Insert data from CSV into user_data table
def insert_data(connection, csv_file):
    try:
        cursor = connection.cursor()
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = str(uuid.uuid4())
                name = row['name']
                email = row['email']
                age = row['age']
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (%s, %s, %s, %s)
                """, (user_id, name, email, age))
        connection.commit()
        cursor.close()
        print(f"Data inserted from {csv_file}")
    except FileNotFoundError:
        print(f"CSV file {csv_file} not found")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
