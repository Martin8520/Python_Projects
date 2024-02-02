def group_by_remainder(array):
    group = [[],
             [],
             []
    ]

    for num in array:
        remainder = num % 3
        group[remainder].append(num)

    return group


array = list(map(int, input().split()))


result = group_by_remainder(array)


for group in result:
    print(" ".join(map(str, group)))
