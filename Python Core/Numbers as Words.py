num = int(input())
words = ""

if num == 0:
    words = "zero"
else:
    a = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
         "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    b = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if num >= 100:
        words += a[num // 100] + " hundred"
        num %= 100
        if num > 0:
            words += " and "
    if num >= 20:
        words += b[num // 10]
        num %= 10
        if num > 0:
            words += " "
    if num > 0:
        words += a[num]

print(words)






