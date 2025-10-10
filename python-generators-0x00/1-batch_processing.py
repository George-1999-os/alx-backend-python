#!/usr/bin/python3
"""
Batch processing of user data using Python generators.
Fetches data in batches and processes users over the age of 25.
"""

import sqlite3


def stream_users_in_batches(batch_size):
    """
    Generator that fetches user data in batches from the database.

    Args:
        batch_size (int): Number of rows to fetch per batch.

    Yields:
        list[dict]: A batch of user dictionaries.
    """
    conn = sqlite3.connect("user_data.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data")
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        yield [dict(row) for row in rows]

    conn.close()


def batch_processing(batch_size):
    """
    Processes each batch of users and prints users over age 25.

    Args:
        batch_size (int): Number of rows per batch.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
