price = float(input())
paid = float(input())

change = float((paid - price) * 100)

coins = [100, 50, 20, 10, 5, 2, 1]

for coins in coins:
    if change >= coins:
        num = change // coins
        if coins == 100:
            print(f"{int(num)} x 1 lev")
        elif coins == 1:
            print(f"{int(num)} x 1 stotinka")
        else:
            print(f"{int(num)} x {coins} stotinki")

        change %= coins





