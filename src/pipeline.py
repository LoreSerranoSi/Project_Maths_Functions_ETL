from extract import extract_data
from transform import process_data
from load import load_data
import argparse
import os
import logging
from logging_config import setup_logging

logger = logging.getLogger(__name__)


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "raw", "input.json")

def get_args():
    parser = argparse.ArgumentParser(description="ETL Pipeline - Math Functions")

    parser.add_argument(
        "--mode",
        type=str,
        default="json",
        choices=["json", "console"],
        help="Execution mode: json (file) or console (interactive)"
    )

    return parser.parse_args()


def get_user_input():
    logger.info("🧠 NUEVO REGISTRO")

    function = input("Function (ej: x**2): ")
    operation = input("Operation (derivative / integral): ")

    return {
        "function": function,
        "operation": operation
    }

def extract_from_console():
    data = []

    while True:
        record = get_user_input()
        data.append(record)

        more = input("\n¿Agregar otro registro? (y/n): ").lower()
        if more != "y":
            break

    return data


def run_pipeline(mode="json"):
    logger.info("🚀 ETL PIPELINE STARTED")

    try:
        #############################################################
        # STEP 1: EXTRACT
        logger.info("📥 STEP 1: EXTRACT")

        if mode == "json":
            data = extract_data(FILE_PATH)

        elif mode == "console":
            data = extract_from_console()

        else:
            logger.error("❌ Invalid mode. Use 'json' or 'console'.")
            return
        
        print("📄 Extracted data:")
        print(data)
        #####################################################
        # STEP 2: TRANSFORM
        logger.info("🔄 STEP 2: TRANSFORM")
        transformed = process_data(data)
        print("📄 Transformed data:")
        print(transformed)
        ######################################################
        # STEP 3: LOAD
        logger.info("💾 STEP 3: LOAD")
        load_data(transformed)
        logger.info("✅ PIPELINE FINISHED SUCCESSFULLY")
        ######################################################
    
    except (FileNotFoundError, ValueError) as e:
        logger.error("❌ Error en la extracción: %s", e)

    except Exception:
        logger.exception("❌ Error inesperado durante el pipeline")


if __name__ == "__main__":
    setup_logging()
    args = get_args()
    run_pipeline(mode=args.mode)