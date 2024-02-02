nums = input().split(',')
nums = [int(x) for x in nums]
N = int(input())

equal_nums = True
mismatched_pairs = []

for i in range(N):
    if nums[i] != nums[-N + i]:
        equal_nums = False
        mismatched_pairs.append((nums[i], nums[-N + i]))

if equal_nums:
    print("True", end=" ")
    print(*nums[:N], sep=",")
else:
    print("False", end=" ")
    for pair in mismatched_pairs:
        print(f"{pair[0]},{pair[1]}", end=" ")
    print()
