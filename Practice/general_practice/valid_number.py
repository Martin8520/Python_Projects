def isNumber(s: str) -> bool:
    states = [
        {'digit': 1, 'dot': 2, 'sign': 3},
        {'digit': 1, 'dot': 4, 'exponent': 5},
        {'digit': 4},
        {'digit': 1, 'dot': 2},
        {'digit': 4, 'exponent': 5},
        {'digit': 7, 'sign': 6},
        {'digit': 7},
        {'digit': 7}
    ]

    current_state = 0

    for char in s:
        if char.isdigit():
            input_type = 'digit'
        elif char == '.':
            input_type = 'dot'
        elif char in ('e', 'E'):
            input_type = 'exponent'
        elif char in ('+', '-'):
            input_type = 'sign'
        else:
            return False

        if input_type not in states[current_state]:
            return False

        current_state = states[current_state][input_type]

    return current_state in (1, 4, 7)


print(isNumber("0"))
print(isNumber("e"))
print(isNumber("."))
