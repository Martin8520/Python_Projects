movement = input().strip()

x = 0
y = 0

for i in movement:
    if i == "R":
        x += 1
    elif i == "L":
        x -= 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1

print(f"({x}, {y})")
