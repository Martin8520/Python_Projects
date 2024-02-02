def generate_image(width, height):

    for i in range(height):

        for j in range(width):
            print("#", end=" ")
        print()


def main():
    print("Image Generator")
    try:
        width = int(input("Enter the image width: "))
        height = int(input("Enter the image height: "))

        if width <= 0 or height <= 0:
            print("Width and height must be positive integers.")
        else:
            generate_image(width, height)
    except ValueError:
        print("Invalid input. Please enter positive integers for width and height.")


if __name__ == "__main__":
    main()
