
#!/usr/bin/env python3
import sqlite3
import functools

query_cache = {}

# Decorator to open/close DB connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

# Decorator to cache query results
def cache_query(func):
    @functools.wraps(func)
    def wrapper(conn, query):
        if query in query_cache:
            print("Using cached result for:", query)
            return query_cache[query]
        print("Executing and caching:", query)
        result = func(conn, query)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Test
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)

# Second call to test cache
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)
