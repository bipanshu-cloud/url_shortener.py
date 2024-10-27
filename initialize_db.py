import sys
import os

# Add the parent directory of the current directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'shortener_app')))

from database import init_db  # Adjust the import based on your package structure

if __name__ == "__main__":
    init_db()  # Initialize the database
    print("Database initialized successfully!")
