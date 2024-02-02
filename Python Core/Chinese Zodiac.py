year = int(input())

cycle = (year - 2000) % 12

if cycle == 0:
    sign = "Dragon"
elif cycle == 1:
    sign = "Snake"
elif cycle == 2:
    sign = "Horse"
elif cycle == 3:
    sign = "Sheep"
elif cycle == 4:
    sign = "Monkey"
elif cycle == 5:
    sign = "Rooster"
elif cycle == 6:
    sign = "Dog"
elif cycle == 7:
    sign = "Pig"
elif cycle == 8:
    sign = "Rat"
elif cycle == 9:
    sign = "Ox"
elif cycle == 10:
    sign = "Tiger"
else:
    sign = "Hare"

print(sign)
