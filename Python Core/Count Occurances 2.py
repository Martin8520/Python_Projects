def occurrences(letter, string):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count


def stronger_letter(text, letter1, letter2):
    count_letter1 = occurrences(letter1, text)
    count_letter2 = occurrences(letter2, text)

    if count_letter1 > count_letter2:
        return letter1
    elif count_letter2 > count_letter1:
        return letter2
    else:
        return letter1


x1 = stronger_letter('abca', 'a', 'b')
print(x1)

x2 = stronger_letter('abbca', 'c', 'b')
print(x2)

x3 = stronger_letter('aabbc', 'b', 'a')
print(x3)
