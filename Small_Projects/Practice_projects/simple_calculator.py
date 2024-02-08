def addition(num1, num2):
    result = num1 + num2
    print(f"The result is: {result:.2f}")


def subtraction(num1, num2):
    result = num1 - num2
    print(f"The result is: {result:.2f}")


def multiplication(num1, num2):
    result = num1 * num2
    print(f"The result is: {result:.2f}")


def division(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"The result is: {result:.2f}")

while True:
    choose_op = input("Input the type of operation you want to use: 'add'/'subtract'/'multiply'/'divide' (or 'exit' to quit): ").lower()

    if choose_op == "exit":
        print("Exiting the calculator. Goodbye!")
        break

    if choose_op in ["add", "subtract", "multiply", "divide"]:
        try:
            num1 = float(input("Input the first number: "))
            num2 = float(input("Input the second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        if choose_op == "add":
            addition(num1, num2)
        elif choose_op == "subtract":
            subtraction(num1, num2)
        elif choose_op == "multiply":
            multiplication(num1, num2)
        elif choose_op == "divide":
            division(num1, num2)
    else:
        print("Invalid input! Please use 'add'/'subtract'/'multiply'/'divide' (or 'exit' to quit')")
