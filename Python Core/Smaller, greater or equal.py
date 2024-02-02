n = int(input())

num = int(input())
str_num = str(num)

for i in range(n - 1):
    num2 = int(input())
    if num2 > num:
        str_num += "<" + str(num2)
    elif num2 < num:
        str_num += ">" + str(num2)
    else:
        str_num += "=" + str(num2)
    num = num2

print(str_num)
