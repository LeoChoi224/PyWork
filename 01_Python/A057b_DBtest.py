from A057a_Database import Database
from dotenv import load_dotenv
load_dotenv()

import os

db = Database()

conn_info = {
    'host': os.getenv('db_host'),
    'user': os.getenv('db_user'),
    'password': os.getenv('db_password'),
    'database': os.getenv('db_database'),
}

db.connect(**conn_info)

print(db.select_one("SELECT * FROM users ORDER BY id DESC"))