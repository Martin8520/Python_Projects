# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

student_num = 0
for height in student_heights:
    student_num += 1
print(f"number of students = {student_num}")

avg_height = total_height / student_num
print(f"average height = {round(avg_height)}")
