a = float(input())
b = float(input())
c = float(input())

if a == 0 or b == 0 or c == 0:
    print("0")
elif (a < 0 and b < 0 and c < 0) or (a > 0 > c and b > 0) or (a > 0 > b and c > 0) or (a < 0 < b and c > 0):
    print("-")
else:
    print("+")
