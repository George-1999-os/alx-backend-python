#!/usr/bin/env python3
"""
Cached user-data streaming generator.

Uses the existing generator chain:
  user_data_generator -> filter_by_age -> obfuscate_email

Keeps a simple in-memory cache (dictionary) of user_id -> user dict so
previously-seen users are not yielded again. When a cached user is
encountered the generator prints a message and continues.
"""

from user_data_generator import user_data_generator
from filter_user_data import filter_by_age
from obfuscate_user_email import obfuscate_email

# simple in-memory cache
cache = {}

def cached_user_data(min_age=50):
    """
    Yield unique (not-yet-cached) users aged >= min_age,
    with obfuscated emails (from obfuscate_email generator).
    """
    for user in obfuscate_email(filter_by_age(min_age)):
        user_id = user.get("user_id")
        if user_id is None:
            # no id: just yield
            yield user
            continue

        if user_id not in cache:
            cache[user_id] = user
            yield user
        else:
            # do not yield again; inform the user
            print(f"Cached user skipped: {user_id}")

if __name__ == "__main__":
    print("Streaming unique users aged 50 and above with obfuscated emails:\n")
    for u in cached_user_data():
        print(u)

    print("\nRunning generator again (should skip cached users):\n")
    for u in cached_user_data():
        # second run will not yield previously-cached users,
        # but the generator prints "Cached user skipped: <id>" for each.
        print(u)
