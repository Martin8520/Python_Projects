print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


name1_lower = name1.lower()
name2_lower = name2.lower()

true_counter = (name1_lower.count("t") + name2_lower.count("t") + name1_lower.count("r") + name2_lower.count("r")
                + name1_lower.count("u") + name2_lower.count("u") + name1_lower.count("e") + name2_lower.count("e"))

love_counter = (name1_lower.count("l") + name2_lower.count("l") + name1_lower.count("o") + name2_lower.count("o")
                + name1_lower.count("v") + name2_lower.count("v") + name1_lower.count("e") + name2_lower.count("e"))

final_score = str(true_counter) + str(love_counter)

if int(final_score) < 10 or int(final_score) > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
elif 40 <= int(final_score) <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"Your score is {final_score}.")

