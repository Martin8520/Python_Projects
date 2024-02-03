programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

empty_dict = {}

# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in my PC."
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 3},
    "Germany": {"cities_visited": ["Berlin", "Munich", "Essen"], "total_visits": 3},
}

travel_log2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 3
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich", "Essen"],
        "total_visits": 3
    },
]

print(travel_log2[1])
