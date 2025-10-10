#!/usr/bin/python3
"""
Batch processing using generators.
"""

import sqlite3


def stream_users_in_batches(batch_size):
    """Yield users in batches from user_data table."""
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
    """Print users older than 25 in each batch."""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user["age"] > 25:
                print(user)
