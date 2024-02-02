numbers = input()
num_str = numbers.split(",")
num_lst = [int(num) for num in num_str]

sum_lst = sum(num_lst)
num_count = len(num_lst)

if num_count > 0:
    avg_num = sum_lst / num_count
    below_avg = []
    above_avg = []

    for i in num_lst:
        if i < avg_num:
            below_avg.append(str(i))
        elif i > avg_num:
            above_avg.append(str(i))

    print(f"avg: {avg_num:.2f}")
    print(f"below: {','.join(below_avg)}")
    print(f"above: {','.join(above_avg)}")
