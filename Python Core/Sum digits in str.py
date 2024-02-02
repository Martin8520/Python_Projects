def sum_digit(str_input):
    return sum(int(ch) for ch in str_input if ch.isdigit())


x1 = sum_digit("abc123a4")
print(x1)

x2 = sum_digit("abc")
print(x2)
