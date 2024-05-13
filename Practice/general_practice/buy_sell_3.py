def maxProfit(prices):
    buy1 = float('-inf')
    sell1 = 0
    buy2 = float('-inf')
    sell2 = 0

    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1,
                    buy1 + price)

        buy2 = max(buy2,
                   sell1 - price)
        sell2 = max(sell2,
                    buy2 + price)

    return sell2


prices1 = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfit(prices1))  # 6

prices2 = [1, 2, 3, 4, 5]
print(maxProfit(prices2))  # 4

prices3 = [7, 6, 4, 3, 1]
print(maxProfit(prices3))  # 0
