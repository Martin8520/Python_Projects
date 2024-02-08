import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = input("Type '1' for Rock, '2' for Paper or '3': ")
computer_input = random.randint(1, 3)

if user_input == "1":
    print(rock)
elif user_input == "2":
    print(paper)
elif user_input == "3":
    print(scissors)

print("Computer chose:")

if computer_input == 1:
    print(rock)
elif computer_input == 2:
    print(paper)
elif computer_input == 3:
    print(scissors)

if (user_input == "1" and computer_input == 1) or (user_input == "2" and computer_input == 2) or (user_input == "3" and computer_input == 3):
    print("Its a draw")
elif (user_input == "1" and computer_input == 2) or (user_input == "2" and computer_input == 3) or (user_input == "3" and computer_input == 1):
    print("You lose")
elif int(user_input) > 3:
    print("Invalid choice. You lose!")
else:
    print("You win")
