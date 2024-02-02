n = input()

n = n.replace(".", "")

negative = n[0] == "-"

if negative:
    n = n[1:]

zero_input = True
for digits in n:
    if digits != "0":
        zero_input = False
        break

if zero_input:
    print("0")
else:
    while int(n) > 9:
        total = 0
        for num in n:
            total += int(num)
        n = str(total)

    print(n)
