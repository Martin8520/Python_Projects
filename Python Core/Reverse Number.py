decimal_number = input()

decimal_str = str(decimal_number)

if '.' in decimal_str:
    integer_part, fractional_part = decimal_str.split('.')
    reversed_integer = int(integer_part[::-1])
    reversed_fractional = fractional_part[::-1]

    print(f"{reversed_fractional}.{reversed_integer}")
else:
    reversed_number = int(decimal_str[::-1])
    print(reversed_number)
