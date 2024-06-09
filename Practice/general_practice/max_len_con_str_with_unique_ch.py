def maxLength(arr):
    def is_unique(s):
        return len(s) == len(set(s))

    def backtrack(index, current):
        if index == len(arr):
            return len(current)
        res = backtrack(index + 1, current)
        if is_unique(current + arr[index]):
            res = max(res, backtrack(index + 1, current + arr[index]))
        return res

    arr = [s for s in arr if is_unique(s)]
    return backtrack(0, "")


arr1 = ["un", "iq", "ue"]
print(maxLength(arr1))  # 4

arr2 = ["cha", "r", "act", "ers"]
print(maxLength(arr2))  # 6

arr3 = ["abcdefghijklmnopqrstuvwxyz"]
print(maxLength(arr3))  # 26
