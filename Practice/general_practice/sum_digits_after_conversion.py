def getLucky(s, k):
    num_str = ''.join(str(ord(c) - ord('a') + 1) for c in s)
    num = sum(int(digit) for digit in num_str)

    for _ in range(k - 1):
        num = sum(int(digit) for digit in str(num))

    return num


s = "iiii"
k = 1
print(getLucky(s, k))

s = "leetcode"
k = 2
print(getLucky(s, k))

s = "zbax"
k = 2
print(getLucky(s, k))
