#!/usr/bin/python3
"""
Generator functions to process user data in batches.
"""

from stream_users import stream_users


def stream_users_in_batches(batch_size):
    """Yield users in batches of a given size."""
    batch = []
    for user in stream_users():
        batch.append(user)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def batch_processing(batch_size):
    """Process batches and print users over age 25."""
    for batch in stream_users_in_batches(batch_size):
        filtered = [user for user in batch if user.get("age", 0) > 25]
        for user in filtered:
            print(user)
