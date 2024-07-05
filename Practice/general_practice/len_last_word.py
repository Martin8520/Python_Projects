def length_of_last_word(s: str) -> int:
    trimmed = s.strip()

    words = trimmed.split()

    if words:
        return len(words[-1])
    return 0


print(length_of_last_word("Hello World"))  # 5
print(length_of_last_word("   fly me   to   the moon  "))  # 4
print(length_of_last_word("luffy is still joyboy"))  # 6
