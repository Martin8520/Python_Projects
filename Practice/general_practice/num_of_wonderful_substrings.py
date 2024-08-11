def wonderfulSubstrings(word):
    count = {0: 1}
    current_mask = 0
    result = 0

    for ch in word:
        current_mask ^= (1 << (ord(ch) - ord('a')))

        result += count.get(current_mask, 0)

        for i in range(10):
            mask_to_check = current_mask ^ (1 << i)
            result += count.get(mask_to_check, 0)

        count[current_mask] = count.get(current_mask, 0) + 1

    return result


word1 = "aba"
word2 = "aabb"
word3 = "he"

print(wonderfulSubstrings(word1))  # 4
print(wonderfulSubstrings(word2))  # 9
print(wonderfulSubstrings(word3))  # 2
