import math


def compute_logarithms(number):
    try:
        base = 10
        log_result = math.log(number, base)
        print(f"log_{base}({number}) = {log_result}")

        natural_log_result = math.log(number)
        print(f"ln({number}) = {natural_log_result}")

        log10_result = math.log10(number)
        print(f"log10({number}) = {log10_result}")

        log2_result = math.log2(number)
        print(f"log2({number}) = {log2_result}")
    except ValueError as e:
        print(f"Error computing logarithms: {e}")


compute_logarithms(100)
compute_logarithms(1)
compute_logarithms(0.5)
compute_logarithms(-10)
