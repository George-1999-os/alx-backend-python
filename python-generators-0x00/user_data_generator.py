#!/usr/bin/env python3
"""
Task 1: Create a generator that yields rows from user_data table
"""

import mysql.connector


def user_data_generator():
    """Generator that yields one row at a time from user_data table."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="georgE@3111",
        database="ALX_prodev"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield row  # yield each row as a dictionary

    cursor.close()
    connection.close()


if __name__ == "__main__":
    for record in user_data_generator():
        print(record)
