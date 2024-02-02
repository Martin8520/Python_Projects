target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

even_num = 0
for num in range(0, target + 1):
    if num % 2 == 0:
        even_num += num
print(even_num)
