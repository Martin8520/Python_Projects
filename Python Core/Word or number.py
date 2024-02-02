word_num = input()

if word_num.isalpha():

    reverse = word_num[::-1]
    print(reverse)
elif word_num.replace(".", "").isdigit() or (word_num[0] == '-' and word_num[1:].replace(".", "").isdigit()):

    is_float = '.' in word_num
    num = float(word_num)

    if is_float:
        num += 1
        print(f"{num}")
    else:
        num = int(word_num) + 1
        print(num)

