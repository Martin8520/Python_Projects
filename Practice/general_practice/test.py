def text_to_uppercase(text):
    return text.upper()


def text_to_lowercase(text):
    return text.lower()


def text_to_title_case(text):
    return text.title()


def text_to_reversed(text):
    return text[::-1]


def display_menu():
    print("\nChoose a transformation:")
    print("1. Convert text to uppercase")
    print("2. Convert text to lowercase")
    print("3. Convert text to title case")
    print("4. Reverse the text")
    print("5. Exit")
    return input("Enter your choice: ")


def main():
    while True:
        choice = display_menu()

        if choice == '1':
            text = input("Enter the text: ")
            transformed_text = text_to_uppercase(text)
            print("Transformed text:", transformed_text)
        elif choice == '2':
            text = input("Enter the text: ")
            transformed_text = text_to_lowercase(text)
            print("Transformed text:", transformed_text)
        elif choice == '3':
            text = input("Enter the text: ")
            transformed_text = text_to_title_case(text)
            print("Transformed text:", transformed_text)
        elif choice == '4':
            text = input("Enter the text: ")
            transformed_text = text_to_reversed(text)
            print("Transformed text:", transformed_text)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
