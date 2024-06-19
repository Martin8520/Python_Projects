def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift


print(rangeBitwiseAnd(5, 7))  # 4
print(rangeBitwiseAnd(0, 0))  # 0
print(rangeBitwiseAnd(1, 2147483647))  # 0
