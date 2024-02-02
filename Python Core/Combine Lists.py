lst_one = input().split(",")
lst_two = input().split(",")

combined_lst = []

for i in range(len(lst_one)):
    combined_lst.append(lst_one[i])
    combined_lst.append(lst_two[i])

print(",".join(combined_lst))

