import sqlite3
from datetime import datetime
import os


#DB_PATH = "data/etl.db"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "etl.db")

def load_data(results):
    try:
        # 🔥 Asegura que la carpeta exista
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                function TEXT,
                operation TEXT,
                result TEXT,
                timestamp TEXT
            )
        """)

        for item in results:
            cursor.execute("""
                INSERT INTO results (function, operation, result, timestamp)
                VALUES (?, ?, ?, ?)
            """, (
                item["function"],
                item["operation"],
                item["result"],
                datetime.now().isoformat()
            ))

        conn.commit()
        print("💾 Datos insertados correctamente")

    except Exception as e:
        print(f"❌ Error en LOAD: {e}")

    finally:
        if 'conn' in locals():
            conn.close()