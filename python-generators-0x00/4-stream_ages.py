#!/usr/bin/python3
"""
Memory-efficient aggregation of user ages using generators.
"""

import sqlite3

def stream_user_ages():
    """Generator that yields user ages one by one from user_data table."""
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row[0]  # age
    conn.close()

def calculate_average_age():
    """Calculate and print the average age using the generator."""
    total = 0
    count = 0
    for age in stream_user_ages():
        total += age
        count += 1
    if count > 0:
        average = total / count
        print(f"Average age of users: {average}")
    else:
        print("No users found.")

if __name__ == "__main__":
    calculate_average_age()
