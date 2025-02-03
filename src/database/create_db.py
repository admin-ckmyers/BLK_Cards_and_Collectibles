import sqlite3
import os

# Database file path
DB_FILE = 'src/database/blk_cards_collectibles.db'

# Schema file path
SCHEMA_FILE = 'src/database/db_schema.sql'

def create_or_update_database():
    # Create the database directory if it doesn't exist
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

    # Connect to the database (this will create it if it doesn't exist)
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    try:
        # Read the schema file
        with open(SCHEMA_FILE, 'r') as schema_file:
            schema_script = schema_file.read()

        # Execute the schema script
        cursor.executescript(schema_script)

        print("Database created/updated successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Commit changes and close the connection
        conn.commit()
        conn.close()

if __name__ == "__main__":
    create_or_update_database()
