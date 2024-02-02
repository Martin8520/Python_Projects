n = int(input())

prime_num_lst = []
for i in range(1, n + 1):
    if i < 2:
        prime_num = False
    else:
        prime_num = True
        for x in range(2, i):
            if i % x == 0:
                prime_num = False
                break
    if prime_num or i == 1:
        prime_num_lst.append(i)

for prime in prime_num_lst:
    rows = ""
    for y in range(1, prime + 1):
        prime_num = True
        if y < 2:
            prime_num = False
        else:
            for x in range(2, y):
                if y % x == 0:
                    prime_num = False
                    break
        if prime_num or y == 1:
            rows += "1"
        else:
            rows += "0"
    print(rows)
