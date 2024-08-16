def findRelativeRanks(score):
    sorted_scores = sorted(enumerate(score), key=lambda x: x[1], reverse=True)

    rank_mapping = {}
    for i, (index, sc) in enumerate(sorted_scores):
        if i == 0:
            rank_mapping[sc] = "Gold Medal"
        elif i == 1:
            rank_mapping[sc] = "Silver Medal"
        elif i == 2:
            rank_mapping[sc] = "Bronze Medal"
        else:
            rank_mapping[sc] = str(i + 1)

    result = [rank_mapping[s] for s in score]

    return result


print(findRelativeRanks([5, 4, 3, 2, 1]))  # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(findRelativeRanks([10, 3, 8, 9, 4]))  # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
