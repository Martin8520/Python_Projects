num_input = input()
num_lst = [int(num) for num in num_input.split(",")]

missing_int = [i for i in range(1, len(num_lst) + 1) if i not in num_lst]

result = ",".join(str(num) for num in sorted(missing_int))
print(result)
