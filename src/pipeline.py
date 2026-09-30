from extract import extract_data
from transform import process_data
from load import load_data
import argparse
import os



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
    print("\n🧠 NUEVO REGISTRO")

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
    print("🚀 ETL PIPELINE STARTED")

    print("\n📥 STEP 1: EXTRACT")

    if mode == "json":
        data = extract_data(FILE_PATH)

    elif mode == "console":
        data = extract_from_console()

    else:
        print("❌ Invalid mode. Use 'json' or 'console'.")
        return
    

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
    args = get_args()
    run_pipeline(mode=args.mode)