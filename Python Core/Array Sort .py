num_str = input()
input_lst = num_str.split(",")

num_lst = [int(x) for x in input_lst]

not_zero = 0

for i in range(len(num_lst)):
    if num_lst[i] != 0:
        temp_val = num_lst[i]
        num_lst[i] = num_lst[not_zero]
        num_lst[not_zero] = temp_val
        not_zero += 1

for i in range(not_zero, len(num_lst)):
    num_lst[i] = 0

output_str = ",".join([str(x) for x in num_lst])

print(output_str)
