def generate_square(width, height):
    for i in range(height):
        print("#" * width)


def generate_triangle(height):
    for i in range(1, height + 1):
        print("#" * i)


def generate_rectangle(width, height):
    for i in range(height):
        print("#" * width)


def main():
    print("Image Generator")
    try:
        width = int(input("Enter the image width: "))
        height = int(input("Enter the image height: "))

        if width <= 0 or height <= 0:
            print("Width and height must be positive integers.")
        else:
            print("Choose a shape:")
            print("1. Square")
            print("2. Triangle")
            print("3. Rectangle")

            choice = int(input("Enter your choice (1/2/3): "))

            if choice == 1:
                generate_square(width, height)
            elif choice == 2:
                generate_triangle(height)
            elif choice == 3:
                generate_rectangle(width, height)
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter positive integers for width and height.")


if __name__ == "__main__":
    main()
