total = 0

while True:
    number_str = input()
    number = int(number_str)

    first_digit = number // 100
    last_digit = number % 10
    middle_digit = (number // 10) % 10

    if middle_digit == first_digit + last_digit:
        total += number
    else:
        break

print(total)
