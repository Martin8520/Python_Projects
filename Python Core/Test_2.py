def solution():
    text = input()
    if len(text) == 1:
        return text
    l = longest_block_start_i = 0
    r = longest_block_end_i = 1
    while r < len(text):
        if text[l] != text[r]:
            if r - l > longest_block_end_i - longest_block_start_i:
                longest_block_start_i, longest_block_end_i = l, r
            l = r
        r += 1

    if r - l > longest_block_end_i - longest_block_start_i:
        longest_block_start_i, longest_block_end_i = l, r

    return text[longest_block_start_i: longest_block_end_i]


print(solution())
