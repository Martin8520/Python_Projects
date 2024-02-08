# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇

score = 0

for el in student_scores:
    if el > score:
        score = el
print(score)
