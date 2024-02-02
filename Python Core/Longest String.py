foods = []
while True:
    food = input()
    if food == "END":
        break
    foods.append(food)


longest_len = 0
longest_food = ""
for food in foods:
    if len(food) >= longest_len:
        longest_len = len(food)
        longest_food = food


print(longest_food)
