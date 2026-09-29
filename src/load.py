import sqlite3
from datetime import datetime

DB_PATH = "data/etl.db"

def load_data(results):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        for item in results:
            cursor.execute("""
                INSERT INTO results (expression, operation, result, timestamp)
                VALUES (?, ?, ?, ?)
            """, (
                item["expression"],
                item["operation"],
                item["result"],
                datetime.now().isoformat()
            ))

        conn.commit()
        print("Datos insertados correctamente")

    except Exception as e:
        print(f"Error en LOAD: {e}")

    finally:
        conn.close()