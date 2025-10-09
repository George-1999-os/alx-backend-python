#!/usr/bin/python3
"""
Generator that streams rows from the user_data table one by one.
"""

import mysql.connector


def stream_users():
    """
    Connects to the MySQL database and yields one row at a time
    from the `user_data` table as a dictionary.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="georgE@3111",  # use your actual MySQL password
            database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
