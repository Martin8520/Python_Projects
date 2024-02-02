num_int = input()
num_list = [int(num) for num in num_int.split(",")]

while num_list:
    max_num = max(num_list)
    num_list.remove(max_num)
    print(max_num, end="")

    if num_list:
        print(", ", end="")

print(*num_list)

