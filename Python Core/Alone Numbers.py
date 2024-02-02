num_input = input().split(", ")
num_lst = [int(i) for i in num_input]
target_num = int(input())

for x in range(1, len(num_lst) - 1):
    if num_lst[x] == target_num and num_lst[x - 1] != target_num and num_lst[x + 1] != target_num:
        num_lst[x] = max(num_lst[x - 1], num_lst[x + 1])

print(num_lst)
