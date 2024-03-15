# numbers = [1, 2, 3, 4, 5]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Martin"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [n * 2 for n in range(1, 5)]
# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

capitalized_names = [name.upper() for name in names if len(name) > 5]
print(capitalized_names)