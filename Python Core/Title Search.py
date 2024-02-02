title = input()
word_num = int(input())
result_lst = []
for i in range(word_num):
    current_word = input()
    result = ""

    for el in title:
        if len(current_word) > 0 and el == current_word[0]:
            current_word = current_word[1:]
        else:
            result += el

    if not current_word:
        title = result
        result_lst.append(result)
    else:
        result_lst.append("No such title found!")

print(*result_lst, sep="\n")
