message = input().strip()

current_length = 0
max_length = 0

for ch in message:
    if not ch.isalpha() and not ch.isdigit() and ch != ' ' and ch != '.':
        current_length += 1
    else:
        max_length = max(max_length, current_length)
        current_length = 0

print(max_length)
