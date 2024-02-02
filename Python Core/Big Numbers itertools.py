from itertools import zip_longest

n1, n2 = map(int, input().split())
list1 = map(int, input().split())
list2 = map(int, input().split())
res, carry = [], 0

for d1, d2 in zip_longest(list1, list2, fillvalue=0):
    sumed_digit = d1 + d2 + carry
    if sumed_digit > 9:
        res.append(sumed_digit % 10)
        carry = 1
    else:
        res.append(sumed_digit)
        carry = 0
print(*res)
