n = int(input())

sum_num = 0

for i in range(n):
    num_val = float(input())
    sum_num += num_val

avr = sum_num / n

print(f"{avr:.2f}")