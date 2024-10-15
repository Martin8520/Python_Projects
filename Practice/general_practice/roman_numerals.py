def intToRoman(num):
    roman_dict = [
        (1000000, '_M'), (900000, '_CM'), (500000, '_D'), (400000, '_CD'),
        (100000, '_C'), (90000, '_XC'), (50000, '_L'), (40000, '_XL'),
        (10000, '_X'), (9000, '_IX'), (5000, '_V'), (4000, '_IV'),
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    roman = ""
    for value, symbol in roman_dict:
        while num >= value:
            roman += symbol
            num -= value
    return roman


def romanToInt(s):
    roman_dict = {
        '_M': 1000000, '_D': 500000, '_C': 100000, '_L': 50000, '_X': 10000, '_V': 5000,
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    total = 0
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i] == '_':
            value = roman_dict[s[i:i + 2]]
            i += 2
        else:
            value = roman_dict[s[i]]
            i += 1

        if total > 0 and value > total:
            total = value - total
        else:
            total += value

    return total


user_input = input("Enter a number or a Roman numeral: ")

if user_input.isdigit():
    print(intToRoman(int(user_input)))
else:
    print(romanToInt(user_input))
