def occurrences(letter, string):
    count = 0
    for ch in string:
        if ch == letter:
            count += 1
    return count


x1 = occurrences('a', 'aaa')
print(x1)

x2 = occurrences('a', 'aabb')
print(x2)

x3 = occurrences('a', 'bbcc')
print(x3)
