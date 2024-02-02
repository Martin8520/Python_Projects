n = int(input())
check_lst = []

for i in range(n):
    lines = input().split(",")
    int_list = [int(num) for num in lines]
    sorted_lst = True

    for x in range(1, len(int_list)):
        if int_list[x] < int_list[x - 1]:
            sorted_lst = False
            break

    check_lst.append(sorted_lst)

for bool_val in check_lst:
    if bool_val:
        print("true")
    else:
        print("false")
