import sqlite3
import os

def create_connection(db_file):
    try:
        db_path = os.path.join(os.path.dirname(__file__), '../database/students.db')
        print(f"Connecting to database at: {db_path}")
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")

def create_table():
    conn = create_connection('database/students.db')
    if conn is None:
        return  # Exit if the connection failed
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll_number TEXT NOT NULL,
                course TEXT NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("Students table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_table()
