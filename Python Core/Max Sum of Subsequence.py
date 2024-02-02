n = int(input())

num_sum = 0
max_sum = float("-inf")

for i in range(n):
    num = int(input())

    num_sum += num

    if num_sum < 0:
        num_sum = 0

    if num_sum > max_sum:
        max_sum = num_sum

print(max_sum)
