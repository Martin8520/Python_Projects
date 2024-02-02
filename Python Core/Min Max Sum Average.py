n = int(input())

min_num = float('inf')
max_num = float('-inf')

total_sum = 0
num_lst = []

for i in range(n):
    num = float(input())
    min_num = min(min_num, num)
    max_num = max(max_num, num)
    total_sum += num
    num_lst.append(num)

average = total_sum / n

print(f"min={min_num:.2f}")
print(f"max={max_num:.2f}")
print(f"sum={total_sum:.2f}")
print(f"avg={average:.2f}")
