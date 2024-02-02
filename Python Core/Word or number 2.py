N = int(input())

sum_int = 0
str_words = None
multiple_words = ""

for i in range(N):
    int_str = input()

    if int_str.isdigit():
        sum_int += int(int_str)
    else:
        if str_words:
            multiple_words += "-"
        multiple_words += int_str
        str_words = True

if str_words:
    print(multiple_words)
    print(sum_int)
else:
    print("no words")
    print(sum_int)








