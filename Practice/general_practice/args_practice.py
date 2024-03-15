def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg

    return total


#
#
# print(multiply(-1))


# def add(x, y):
#     return x + y
#
# nums = [3, 5]
#
# print(add(*nums))

# def add(x, y):
#     return x + y
#
#
# nums = {"x": 15, "y": 25}
# print(add(**nums))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="*"))
