def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


prices1 = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices1))

prices2 = [7, 6, 4, 3, 1]
print(maxProfit(prices2))
