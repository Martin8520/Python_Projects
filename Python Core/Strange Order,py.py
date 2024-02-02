num_input = input().split(",")
num_lst = [str(num) for num in num_input]

sorted_lst = sorted(num_lst)
print(*sorted_lst, sep=",")
