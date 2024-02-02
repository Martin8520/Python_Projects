cables_str = input().split()
cables = [int(cable) for cable in cables_str]

trims = 0

min_len = float("inf")
for cable in cables:
    if 0 < cable < min_len:
        min_len = cable

max_len = max(cables)
for i in range(len(cables)):
    if cables[i] == max_len:
        cables[i] -= (max_len - min_len)
        trims += 1

    for x in range(len(cables)):
        if cables[x] > 0:
            cables[x] -= min_len
    trims += min_len

print(trims)
