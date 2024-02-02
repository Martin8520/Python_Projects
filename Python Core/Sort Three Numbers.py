a = int(input())
b = int(input())
c = int(input())

if a >= b >= c:
    print(a, b, c)
else:
    print(a, c, b)
    if b >= a >= c:
        print(b, a, c)
    else:
        print(b, c, a)
        if c >= a >= b:
            print(c, a, b)
        else:
            print(c, b, a)
