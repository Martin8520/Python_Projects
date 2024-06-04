import math

# Logarithm of a number with a specified base
number = 100
base = 10
log_result = math.log(number, base)
print(f"log_{base}({number}) = {log_result}")

# Natural logarithm (base e)
natural_log_result = math.log(number)
print(f"ln({number}) = {natural_log_result}")

# Logarithm base 10
log10_result = math.log10(number)
print(f"log10({number}) = {log10_result}")

# Logarithm base 2
log2_result = math.log2(number)
print(f"log2({number}) = {log2_result}")
