nums = input().split(',')
nums = [int(x) for x in nums]
N = int(input())

equal_nums = True
not_matching_nums = []

for i in range(N):
    if nums[i] != nums[-N + i]:
        equal_nums = False
        not_matching_nums.append(nums[i])

if equal_nums:
    print("true", end=" ")
    print(*nums[:N], sep=",")
else:
    print("false", end=" ")
    print(*not_matching_nums, sep=",")
