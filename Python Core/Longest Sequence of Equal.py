N = int(input())
nums = [int(input()) for num in range(N)]

max_length = 1
current_length = 1
result = None

for i in range(1, N):
    if nums[i] == nums[i - 1]:
        current_length += 1
    else:
        current_length = 1

    max_length = max(max_length, current_length)

result = max_length
print(result)
