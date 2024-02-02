a = int(input())

if 1 <= a <= 3:
    a = a * 10
    print(a)
elif 4 <= a <= 6:
    a = a * 100
    print(a)
elif 7 <= a <= 9:
    a = a * 1000
    print(a)
else:
    print("invalid score")

