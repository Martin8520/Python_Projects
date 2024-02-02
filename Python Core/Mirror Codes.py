n_str = input()

num_as_str = n_str.split()

if len(num_as_str) == 2 and num_as_str[0].isdigit() and num_as_str[1].isdigit():
    num1 = int(num_as_str[0])
    num2 = int(num_as_str[1])

    reversed_num1 = int(str(num1)[::-1])
    reversed_num2 = int(str(num2)[::-1])

    if reversed_num1 > reversed_num2:
        print(reversed_num1)
    else:
        print(reversed_num2)

