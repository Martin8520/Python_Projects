word = input()

n = int(input())

result_lst = []

for i in range(n):
    check_word = input()

    if len(word) == len(check_word) and sorted(word) == sorted(check_word):
        result_lst.append("Yes")
    else:
        result_lst.append("No")

print("\n".join(result_lst))
