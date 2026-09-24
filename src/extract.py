import json
import os

def extract_data(file_path: str):
    """
    Lee archivo JSON que contiene múltiples registros
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        raise ValueError("El JSON tiene formato inválido")

    # Validar que sea lista
    if not isinstance(data, list):
        raise ValueError("El JSON debe ser una lista de registros")

    # Validar campos de cada registro
    required_fields = ["function", "operation"]

    for i, item in enumerate(data):
        for field in required_fields:
            if field not in item:
                raise ValueError(f"Falta el campo '{field}' en el registro {i}")

    return data