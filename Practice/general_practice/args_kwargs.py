def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5, 20, 15, 33, 12, 6, 2, 8))


def calculate(n, **kwargs):

    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.seats = kwargs.get("seats")



my_car = Car(seats=5)
print(my_car.seats)