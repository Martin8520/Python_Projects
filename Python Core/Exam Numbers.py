x = int(input())
y = int(input())
t = int(input())

for num in range(x, y + 1):
    if 100 <= num <= 999:
        sum_digit = sum(int(digit) for digit in str(num))
        while sum_digit == t:
            print(num)
            break
