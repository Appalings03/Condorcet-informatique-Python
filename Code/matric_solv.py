from fractions import Fraction
import sys
import numpy as np


def read_vector(size, label):
    values = input(f"{label} ({size} values, separated by spaces): ").split()
    if len(values) != size:
        raise ValueError(f"Expected {size} values, got {len(values)}.")
    return np.array([float(v) for v in values], dtype=float)


def format_solution_value(value):
    value = float(value)
    if np.isfinite(value):
        fraction = Fraction(value).limit_denominator(10_000)
        if np.isclose(float(fraction), value, rtol=1e-10, atol=1e-12):
            return str(fraction)
    return str(value)


try:
    size = int(input("Input matrix size: "))
    if size <= 0:
        raise ValueError("Matrix size must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}",e)
    sys.exit(1)

try:
    A = np.zeros((size, size), dtype=float)
    for i in range(size):
        A[i] = read_vector(size, f"Row {i + 1} of matrix A")

    b = read_vector(size, "Right-hand side vector b")
    solution = np.linalg.solve(A, b)
    print("Solution x:")
    print("[" + " ".join(format_solution_value(value) for value in solution) + "]")
except ValueError as exc:
    print(f"Invalid input: {exc}")
    sys.exit(1)
except np.linalg.LinAlgError:
    print("The system has no unique solution.")
    sys.exit(1)