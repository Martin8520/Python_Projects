def grayCode(n):
    result = [0]
    for i in range(n):
        result += [x + 2 ** i for x in reversed(result)]
    return result


print(grayCode(2))
print(grayCode(1))
