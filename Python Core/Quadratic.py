a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
x1 = (-b - (D ** 0.5)) / (2 * a)
x2 = (-b + (D ** 0.5)) / (2 * a)
print(f"x1={x1+0:.1f}")
print(f"x2={x2+0:.1f}")

