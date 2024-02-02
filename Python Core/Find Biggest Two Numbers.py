numbers = input().split()
numbers = [int(num) for num in numbers]

largest_num = -float("inf")
second_largest_num = -float("inf")

for num in numbers:
    if num > largest_num:
        second_largest_num = largest_num
        largest_num = num
    elif num > second_largest_num and num != largest_num:
        second_largest_num = num
    elif num == largest_num:
        second_largest_num = num

print(largest_num, second_largest_num)
