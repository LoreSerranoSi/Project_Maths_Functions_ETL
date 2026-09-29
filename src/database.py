import sqlite3
import os

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, "etl.db")

print("DB PATH", DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expression TEXT NOT NULL,
    operation TEXT NOT NULL,
    result TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("✔ DB creada correctamente en:", DB_PATH)