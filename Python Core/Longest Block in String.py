def find_longest_str(x):
    if not x:
        return ""

    max_block = ""
    current_block = ""
    current_ch = ""

    for char in x:
        if char == current_ch:
            current_block += char
        else:
            current_ch = char
            current_block = char

        if len(current_block) > len(max_block):
            max_block = current_block

    return max_block


input_str = input()

result = find_longest_str(input_str)
print(result)
