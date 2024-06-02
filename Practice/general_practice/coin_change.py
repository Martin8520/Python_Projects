def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1


coins1 = [1, 2, 5]
amount1 = 11
print(coin_change(coins1, amount1))  # 3

coins2 = [2]
amount2 = 3
print(coin_change(coins2, amount2))  # -1

coins3 = [1]
amount3 = 0
print(coin_change(coins3, amount3))  # 0
