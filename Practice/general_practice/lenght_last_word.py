def length_of_last_word(s):
    s = s.rstrip()

    last_space_index = s.rfind(' ')

    if last_space_index == -1:
        return len(s)
    else:
        return len(s) - last_space_index - 1


print(length_of_last_word("Hello World"))
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("luffy is still joyboy"))
