import sqlite3
from datetime import datetime
import os
import logging

logger = logging.getLogger(__name__)

# DB_PATH = "data/etl.db"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "etl.db")


def load_data(results):
    try:
        # Asegura que la carpeta exista
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


        inserted = 0
        duplicated = 0
        for item in results:

            cursor.execute("""
                SELECT 1 FROM results
                WHERE function = ?
                AND operation = ?
                AND result = ?
            """, (
                item["function"],
                item["operation"],
                item["result"]
            ))

            if cursor.fetchone() is None:
                cursor.execute("""
                    INSERT INTO results (function, operation, result, timestamp)
                    VALUES (?, ?, ?, ?)
                """, (
                    item["function"],
                    item["operation"],
                    item["result"],
                    datetime.now().isoformat()
                ))
                inserted += 1
            else:
                duplicated += 1
                logger.warning(
                    f"⚠️ Registro duplicado omitido: "
                    f"{item['function']} - {item['operation']}"
                )

        conn.commit()
        logger.info(
            f"💾 LOAD FINALIZADO: {inserted} insertados, "
            f"{duplicated} duplicados"
        )

    except Exception as e:
        logger.error(f"❌ Error en LOAD: {e}")

    finally:
        if 'conn' in locals():
            conn.close()
