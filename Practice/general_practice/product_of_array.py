def productExceptSelf(nums):
    length = len(nums)
    answer = [0] * length

    answer[0] = 1
    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    r = 1
    for i in reversed(range(length)):
        answer[i] = answer[i] * r
        r *= nums[i]

    return answer


print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
print(productExceptSelf([0, 0]))  # [0, 0]
print(productExceptSelf([1, 0]))  # [0, 1]
print(productExceptSelf([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
