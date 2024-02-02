lst_one = [int(x) for x in input().split(',')]
lst_two = [int(x) for x in input().split(',')]

result = []

for num in lst_one:
    found = False

    for next_num in lst_two[lst_two.index(num):]:
        if next_num > num:
            result.append(next_num)
            found = True
            break

    if not found:
        result.append(-1)

print(','.join(str(x) for x in result))
