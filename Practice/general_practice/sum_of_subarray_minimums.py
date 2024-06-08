def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    n = len(arr)

    left = [0] * n
    right = [0] * n

    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        left[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    stack = []
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        right[i] = n - i if not stack else stack[-1] - i
        stack.append(i)

    result = 0
    for i in range(n):
        result = (result + arr[i] * left[i] * right[i]) % MOD

    return result

arr1 = [3, 1, 2, 4]
print(sumSubarrayMins(arr1))  # 17

arr2 = [11, 81, 94, 43, 3]
print(sumSubarrayMins(arr2))  # 444
