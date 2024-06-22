def bagOfTokensScore(tokens, power):
    tokens.sort()
    left, right = 0, len(tokens) - 1
    score = 0
    max_score = 0

    while left <= right:
        if power >= tokens[left]:
            # Play the token face-up
            power -= tokens[left]
            score += 1
            left += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return max_score


print(bagOfTokensScore([100], 50))  # 0
print(bagOfTokensScore([200, 100], 150))  # 1
print(bagOfTokensScore([100, 200, 300, 400], 200))  # 2
