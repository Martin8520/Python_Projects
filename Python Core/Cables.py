# Input
cables_input = input().split()
cables = [int(cable) for cable in cables_input]

# Initialize trims counter
trims = 0

# Trim the longest cable to reach the minimum length
max_length = max(cables)

# Identify the initial minimum length of non-zero cables
min_length = min((cable for cable in cables if cable > 0), default=0)

while max_length > min_length:
    for i in range(len(cables)):
        if cables[i] == max_length:
            cables[i] -= 1
            trims += 1

    max_length = max(cables)

# Trim all cables by the length of the new shortest cable
while min_length > 0:
    for i in range(len(cables)):
        if cables[i] > 0:
            cables[i] -= min_length
    trims += min_length

    # Identify the new minimum length of non-zero cables
    min_length = min((cable for cable in cables if cable > 0), default=0)

# Output the total number of trims
print(trims)
