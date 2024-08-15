def compareVersion(version1, version2):
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))

    max_len = max(len(v1), len(v2))
    v1.extend([0] * (max_len - len(v1)))
    v2.extend([0] * (max_len - len(v2)))

    for i in range(max_len):
        if v1[i] > v2[i]:
            return 1
        elif v1[i] < v2[i]:
            return -1

    return 0


print(compareVersion("1.2", "1.10"))  # -1
print(compareVersion("1.01", "1.001"))  # 0
print(compareVersion("1.0", "1.0.0.0"))  # 0
