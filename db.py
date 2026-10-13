
import sqlite3
from contextlib import contextmanager

DATABASE_NAME = "users.db"


def get_db_connection():
    """Create and return a database connection."""
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_tables():
    """Create the users table if it does not exist."""
    connection = get_db_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        """)
        connection.commit()
    finally:
        connection.close()


@contextmanager
def get_db():
    """Provide a database connection and close it afterward."""
    connection = get_db_connection()

    try:
        yield connection
    finally:
        connection.close()


if __name__ == "__main__":
    create_tables()
    print("Database and users table created successfully.")
