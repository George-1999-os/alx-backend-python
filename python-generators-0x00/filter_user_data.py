#!/usr/bin/env python3
"""
Task 2: Chain generators to filter user data
"""

from decimal import Decimal
from user_data_generator import user_data_generator


def filter_by_age(min_age=50):
    """Generator that filters users older than min_age."""
    for user in user_data_generator():
        if user["age"] >= Decimal(min_age):
            yield user


if __name__ == "__main__":
    print(f"Users aged 50 and above:\n")
    for record in filter_by_age(50):
        print(record)
