# def format_name(f_name, l_name):
#     formated_l = l_name.title()
#     formated_f = f_name.title()
#     return f"{formated_f} {formated_l}"
#
#
# formated_str = format_name("JOhn", "DOE")
#
# print(formated_str)


# def add(x, y):
#     return x + y
#
#
# print(add(5, 7))
#
# add = lambda x, y: x + y
# print(add(5, 10))
#
# print((lambda x, y: x + y)(20, 80))


def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [(lambda x: x * 2)(x) for x in sequence]
print(doubled)

doubled2 = list(map(double, sequence))
print(doubled2)
