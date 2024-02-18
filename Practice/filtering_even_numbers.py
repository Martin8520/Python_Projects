list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
list_of_nums = [int(num) for num in list_of_strings]
result = [num for num in list_of_nums if num % 2 == 0]



# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"


# Write your code 👆 above:
print(result)