n = int(input())

result = [str(num) for num in range(1, n + 1) if num % 3 != 0 and num % 7 != 0]

print(" ".join(result))
