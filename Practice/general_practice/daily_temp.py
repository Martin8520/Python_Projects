def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    return answer


temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures1))  # [1, 1, 4, 2, 1, 1, 0, 0]

temperatures2 = [30, 40, 50, 60]
print(dailyTemperatures(temperatures2))  # [1, 1, 1, 0]

temperatures3 = [30, 60, 90]
print(dailyTemperatures(temperatures3))  # [1, 1, 0]
