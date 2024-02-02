card = input()

deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

if card in deck:
    print("yes")
elif card.isupper():
    print("yes")
else:
    print("no")



