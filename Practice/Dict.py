# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
#
# print(programming_dictionary)
#
# programming_dictionary["Loop"] = "The action of doing something over and over again."
#
# print(programming_dictionary)
#
# empty_dict = {}
#
# # programming_dictionary = {}
# # print(programming_dictionary)
#
# programming_dictionary["Bug"] = "A moth in my PC."
# print(programming_dictionary)
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 3},
#     "Germany": {"cities_visited": ["Berlin", "Munich", "Essen"], "total_visits": 3},
# }
#
# travel_log2 = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 3
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Munich", "Essen"],
#         "total_visits": 3
#     },
# ]
#
# print(travel_log2[1])


# Define a list of dictionaries
list_of_dicts = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'firstname': 'Bob', 'surname': 'Smith', 'age': 25, 'city': 'Los Angeles'},
    {'first_name': 'Charlie', 'last_name': 'Brown', 'age': 35, 'city': 'Chicago'}
]

# Specify the keys you want to retrieve from each dictionary
keys_to_get = ['name', 'age', 'city']

# Iterate through the list of dictionaries
for dictionary in list_of_dicts:
    # Initialize an empty list to store the values for the specified keys
    values_for_keys = []
    # Iterate through the keys to get
    for key in keys_to_get:
        # Get the value for the current key from the current dictionary
        value = dictionary.get(key)
        # Append the value to the list
        values_for_keys.append(value)
    # Print the values obtained for the specified keys
    print(values_for_keys)
