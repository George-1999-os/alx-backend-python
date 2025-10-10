#!/usr/bin/python3
"""
A generator function that streams rows from the user_data table one by one.
"""

import sqlite3


def stream_users():
    """
    Connects to a local SQLite database and yields rows from user_data table.

    Yields:
        dict: Each user's data as a dictionary.
    """
    conn = sqlite3.connect("user_data.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield dict(row)

    conn.close()
