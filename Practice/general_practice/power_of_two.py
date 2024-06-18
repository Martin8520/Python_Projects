def isPowerOfTwo(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0


print(isPowerOfTwo(1))  # True
print(isPowerOfTwo(16))  # True
print(isPowerOfTwo(3))  # False
