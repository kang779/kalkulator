# database.py

# Importing necessary libraries
import sqlite3
from sqlite3 import Error

# Function to create a database connection

def create_connection(db_file):
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to '{db_file}' has been established.")
    except Error as e:
        print(e)
    return conn

# Function to create tables

def create_tables(conn):
    """ create products, categories, and transactions tables """
    try:
        cursor = conn.cursor()
        # Create products table
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            category_id INTEGER,
                            price REAL NOT NULL,
                            FOREIGN KEY (category_id) REFERENCES categories (id)
                        );' )
        # Create categories table
        cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL
                        );' )
        # Create transactions table
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            product_id INTEGER NOT NULL,
                            quantity INTEGER NOT NULL,
                            total_price REAL NOT NULL,
                            transaction_date TEXT NOT NULL,
                            FOREIGN KEY (product_id) REFERENCES products (id)
                        );' )
        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print(e)

# Main function to initialize the database

def main():
    database = "kalkulator.db"  # Database name
    conn = create_connection(database)

    if conn:
        create_tables(conn)
        conn.close()

if __name__ == '__main__':
    main()
