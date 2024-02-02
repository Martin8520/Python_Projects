num_lst = [int(x) for x in input().split()]

wave = True

for i in range(len(num_lst)):
    if i % 2 == 0:
        if (i > 0 and num_lst[i] <= num_lst[i - 1]) or (i < len(num_lst) - 1 and num_lst[i] <= num_lst[i + 1]):
            wave = False
            break
    else:
        if (i > 0 and num_lst[i] >= num_lst[i - 1]) or (i < len(num_lst) - 1 and num_lst[i] >= num_lst[i + 1]):
            wave = False
            break

if wave:
    print("yes")
else:
    print("no")
