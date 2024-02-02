L = input()
R = int(input())

square = ord(L) - ord("a") + R

if square % 2 == 0:
    print("light")
else:
    print("dark")
