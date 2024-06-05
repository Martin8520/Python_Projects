import math


def compute_logarithms():
    try:
        number = float(input("Enter the number: "))
        base = float(input("Enter the base (enter 'e' for natural logarithm): "))

        if base == 'e':
            log_result = math.log(number)
            print(f"ln({number}) = {log_result}")
        else:
            base = float(base)
            if base <= 0 or number <= 0:
                raise ValueError("Both number and base must be positive.")
            log_result = math.log(number, base)
            print(f"log_{base}({number}) = {log_result}")

        log10_result = math.log10(number)
        log2_result = math.log2(number)
        print(f"log10({number}) = {log10_result}")
        print(f"log2({number}) = {log2_result}")

    except ValueError as e:
        print(f"Error: {e}")


compute_logarithms()
