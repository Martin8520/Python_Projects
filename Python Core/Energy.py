n = input()

sum_even = 0
sum_odd = 0

for i in n:
    if int(i) % 2 == 0:
        sum_even += int(i)
    else:
        sum_odd += int(i)

if sum_even > sum_odd:
    print(f"{sum_even} energy drinks")
elif sum_even < sum_odd:
    print(f"{sum_odd} cups of coffee")
else:
    print(f"{sum_even} of both")
