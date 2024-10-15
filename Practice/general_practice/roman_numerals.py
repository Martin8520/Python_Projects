def romanToInt(s):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_dict[char]
        if value >= prev_value:
            total += value
        else:
            total -= value
        prev_value = value

    return total


print(romanToInt("XIV"))
print(romanToInt("xiv"))
print(romanToInt("MMXXIV"))
print(romanToInt("mmxxiv"))
