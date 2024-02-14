# with open("my_file") as file:
#     contents = file.read()
#     print(contents)
#


with open("my_file", mode="a") as file:
    file.write("\nHello! How are you?")

with open("new_file", mode="w") as file:
    file.write("NEW TEXT")
