def maximumOddBinaryNumber(s: str) -> str:
    count_1 = s.count('1')
    count_0 = len(s) - count_1

    result = '1' * (count_1 - 1) + '0' * count_0 + '1'

    return result


print(maximumOddBinaryNumber("010"))  # "001"
print(maximumOddBinaryNumber("0101"))  # "1001"
print(maximumOddBinaryNumber("110"))  # "101"
print(maximumOddBinaryNumber("0110"))  # "1001"
