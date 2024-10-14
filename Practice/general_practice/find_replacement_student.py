def chalkReplacer(chalk, k):
    total_chalk = sum(chalk)
    k %= total_chalk
    for i, c in enumerate(chalk):
        if k < c:
            return i
        k -= c

chalk = [5,1,5]
k = 22
print(chalkReplacer(chalk, k))

chalk = [3,4,1,2]
k = 25
print(chalkReplacer(chalk, k))
