def productExceptSelf(nums):
    n = len(nums)
    if n == 0:
        return []

    left_products = [1] * n
    right_products = [1] * n
    output = [1] * n

    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    for i in range(n):
        output[i] = left_products[i] * right_products[i]

    return output


print(productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
print(productExceptSelf([4, 5, 1, 8, 2]))  # [80,64,320,40,160]
print(productExceptSelf([1, 0]))  #: [0,1]
print(productExceptSelf([0, 0]))  # [0,0]
print(productExceptSelf([2, 3, 4, 5]))  # [60,40,30,24]
