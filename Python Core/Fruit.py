n = int(input())

oranges = 0
apples = 0

for k in range(1, n + 1):
    amount_fruit = k * k

    if k % 2 == 0:
        oranges += amount_fruit
    else:
        apples += amount_fruit

fruit_diff = oranges - apples

print(fruit_diff)




