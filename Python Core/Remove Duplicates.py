num_input = input().split(",")
num_lst = [str(num) for num in num_input]
no_dupl_lst = []
for el in num_lst:
    if el not in no_dupl_lst:
        no_dupl_lst.append(el)

print(*no_dupl_lst, sep=",")
