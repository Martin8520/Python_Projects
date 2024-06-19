def findJudge(n: int, trust: list) -> int:
    if n == 1:
        return 1 if not trust else -1

    trusts = [0] * (n + 1)
    trusted_by = [0] * (n + 1)

    for a, b in trust:
        trusts[a] += 1
        trusted_by[b] += 1

    for person in range(1, n + 1):
        if trusts[person] == 0 and trusted_by[person] == n - 1:
            return person

    return -1


print(findJudge(2, [[1, 2]]))  # 2
print(findJudge(3, [[1, 3], [2, 3]]))  # 3
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]))  # -1
