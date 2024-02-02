friends = ["John", "Jim", "Jeremy", "James", "Jake", "Jake", "Jill"]
numbers = [5, 3, 11, 2, 13, 293, 44, 13, 85, 21]

friends.extend(numbers)
friends.append("Jeff")
friends.insert(1, "Joseph")
friends.remove("Jeff")
#friends.clear()
friends.pop()

print(friends.index("Jim"))
print(friends)
print(friends[2])
print(friends.count("Jake"))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
print(numbers2)
