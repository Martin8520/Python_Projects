print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
num_people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? "))

split = total_bill / num_people

tip = split * (percentage / 100)

sum_per_person = tip + split

print(f"Each person should pay: ${sum_per_person:.2f}")
