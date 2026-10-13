
import sqlite3
import os
import logging

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "etl.db")


def get_results():
    """Obtiene todos los resultados almacenados en SQLite."""
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row

            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, function, operation, result, timestamp
                FROM results
                ORDER BY id DESC
            """)

            results = [dict(row) for row in cursor.fetchall()]

        logger.info("Consulta completada: %s registros", len(results))
        return results

    except sqlite3.Error:
        logger.exception("Error al consultar los resultados de SQLite")
        raise
    