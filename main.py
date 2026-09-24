import os
from src.extract import extract_data

def run_etl():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "raw", "input.json")

    dataset = extract_data(file_path)

    print("\n🚀 PROCESANDO DATASET\n")

    for i, record in enumerate(dataset, start=1):
        print(f"Registro {i}:")
        print(record)
        print("-" * 40)

if __name__ == "__main__":
    run_etl()