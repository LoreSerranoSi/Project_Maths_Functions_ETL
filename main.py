import os
from src.extract import extract_data
from src.transform import *
from src.load import load_data


def run_etl():
    #=========================#
    # ETAPA EXTRACT
    #=========================#
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "data", "raw", "input.json")

    dataset = extract_data(file_path)

    print("\n🚀 PROCESANDO DATASET\n")

    for i, record in enumerate(dataset, start=1):
        print(f"Registro {i}:")
        print(record)
        print("-" * 40)

        # =========================
        # ETAPA TRANSFORM
        # =========================

        expression = record["function"]
        operation = record["operation"]

        if operation == "derivative":
            result = calculate_derivative(expression, "x")

        elif operation == "integral":
            result = calculate_integral(expression, "x")

        else:
            print("Operación no soportada")
            continue

        # =========================
        # ETAPA LOAD
        #=========================

        load_data([
            {
                "expression": expression,
                "operation": operation,
                "result": result
            }
        ])


if __name__ == "__main__":
    run_etl()