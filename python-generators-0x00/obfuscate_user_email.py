#!/usr/bin/env python3
"""
Task 3: Chain generators to obfuscate user email addresses
"""

from decimal import Decimal
from user_data_generator import user_data_generator


def filter_by_age(min_age=50):
    """Generator that filters users older than min_age."""
    for user in user_data_generator():
        if user["age"] >= Decimal(min_age):
            yield user


def obfuscate_email(users):
    """Generator that masks user email addresses."""
    for user in users:
        email = user["email"]
        local, domain = email.split("@")
        # Keep only first 2 letters, replace rest with asterisks
        masked_local = local[:2] + "***"
        user["email"] = f"{masked_local}@{domain}"
        yield user


if __name__ == "__main__":
    print("Users aged 50 and above (with obfuscated emails):\n")
    for record in obfuscate_email(filter_by_age(50)):
        print(record)
