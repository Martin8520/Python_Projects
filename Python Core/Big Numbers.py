def size_of_arrays(size, arr1, arr2):
    carry = 0
    result = []

    i = 0
    while i < size or carry > 0:
        digit1 = arr1[i] if i < len(arr1) else 0
        digit2 = arr2[i] if i < len(arr2) else 0

        total = digit1 + digit2 + carry
        result.append(total % 10)
        carry = total // 10

        i += 1

    return result


size1, size2 = map(int, input().split())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))

result_array = size_of_arrays(max(size1, size2), array1, array2)

print(*result_array)
