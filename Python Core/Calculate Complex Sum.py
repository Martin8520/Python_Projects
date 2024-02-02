n = int(input())
x = float(input())

result = 1.0
current = 1.0

for i in range(1, n + 1):
    current *= i / x
    result += current

print("{:.5f}".format(result))
