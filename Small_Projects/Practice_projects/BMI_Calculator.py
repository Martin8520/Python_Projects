# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

BMI = float(weight) / (float(height)**2)

if BMI < 18.5:
    print(f"Your BMI is {BMI:.1f}, you are underweight")
elif 18.5 < BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI:.1f}, you are slightly overweight.")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI:.1f}, you are are obese.")
else:
    print(f"Your BMI is {BMI:.1f}, you are clinically obese.")

