def text_to_numbers(text):
    """Convert text to a list of ASCII values."""
    return [ord(char) for char in text]


def numbers_to_text(numbers):
    """Convert a list of ASCII values to text."""
    return ''.join(chr(num) for num in numbers)


def main():
    while True:
        print("\nChoose an option:")
        print("1. Convert text to numbers")
        print("2. Convert numbers to text")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter the text: ")
            number_output = text_to_numbers(text)
            print("Converted to numbers:", number_output)
        elif choice == '2':
            numbers = input("Enter the numbers (comma-separated): ")
            number_list = [int(num) for num in numbers.split(',')]
            text_output = numbers_to_text(number_list)
            print("Converted to text:", text_output)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
