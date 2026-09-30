from extract import extract_data
from transform import process_data
from load import load_data

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE_PATH = os.path.join(BASE_DIR, "data", "raw", "input.json")


def run_pipeline():
    print("🚀 ETL PIPELINE STARTED")

    print("\n📥 STEP 1: EXTRACT")
    data = extract_data(FILE_PATH)

    print("\n📄 Extracted data:")
    print(data)

    # STEP 2: TRANSFORM
    print("\n🔄 STEP 2: TRANSFORM")
    transformed = process_data(data)
    print("\n📄 Transformed data:")
    print(transformed)

    # STEP 3: LOAD
    print("\n💾 STEP 3: LOAD")
    load_data(transformed)
    print("\n✅ PIPELINE FINISHED SUCCESSFULLY")


if __name__ == "__main__":
    run_pipeline()