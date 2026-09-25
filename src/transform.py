
"""
Módulo de transformación:
Se encarga de procesar expresiones matemáticas
y calcular derivadas e integrales.
"""

from sympy import symbols, diff, integrate, sympify

def normalize_output(result):
    try:
        return str(result).replace("**", "^")
    except Exception:
        return "Invalid output format"


def calculate_derivative(expression, variable):
    try:
        var = symbols(variable)
        expr = sympify(expression)
        derivative = diff(expr, var)
        return normalize_output(derivative)
    except Exception as e:
        return f"Error: {str(e)}"


def calculate_integral(expression, variable):
    try:
        var = symbols(variable)
        expr = sympify(expression)
        integral = integrate(expr, var)
        return normalize_output(integral)
    except Exception as e:
        return f"Error: {str(e)}"

