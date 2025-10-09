# Python Generators Project

This project demonstrates the use of Python generators to handle data efficiently using lazy evaluation.  
It includes practical examples of data streaming, filtering, obfuscation, and caching.

## Files Included
- `0-main.py`: Initializes the MySQL database and table, and inserts data from `user_data.csv`.
- `user_data_generator.py`: Streams user data records from the database.
- `filter_user_data.py`: Filters user data based on age using a generator.
- `obfuscate_user_email.py`: Obfuscates email addresses for privacy while streaming.
- `cached_user_data.py`: Implements a generator that caches processed users to avoid duplication.
- `seed.py`: Seeds the database with CSV data.
- `user_data.csv`: Source data for the project.

## How to Run
1. Ensure MySQL is running and accessible via your configured credentials.
2. Run `python 0-main.py` to initialize the database.
3. Run each subsequent script in sequence to test the generator features.

## Author
George Ibuchi
