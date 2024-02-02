n = int(input())

count_num_lst = [0] * 10

max_count = 0
num_result = 10

for i in range(n):
    num = int(input())
    count_num_lst[num - 1] += 1

    if count_num_lst[num - 1] > max_count or (count_num_lst[num - 1] == max_count and num < num_result):
        max_count = count_num_lst[num - 1]
        num_result = num

print(num_result)
