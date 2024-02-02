variable = input()
a = input()
if variable == "integer":
    print(int(a) + 1)
if variable == "real":
    a = float(a)
    format_a = f"{a:.2f}"
    result = float(format_a) + 1
    print(f"{result:.2f}")
if variable == "text":
    print(f"{str(a)}*")

# else: is not necessary
# else:
#    None











