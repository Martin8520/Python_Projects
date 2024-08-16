def maxHappinessSum(happiness, k):
    happiness.sort(reverse=True)

    max_sum = 0
    total_decrement = 0

    for i in range(k):
        max_sum += happiness[i] - total_decrement

        if i < len(happiness):
            total_decrement += 1

    return max_sum


print(maxHappinessSum([1, 2, 3], 2))  # 4
print(maxHappinessSum([1, 1, 1, 1], 2))  # 1
print(maxHappinessSum([2, 3, 4, 5], 1))  # 5
