# class Animal:
#     def __init__(self):
#         self.num_eyes = 2
#
#     def breathe(self):
#         print("Inhale, exhale.")
#
#
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def breathe(self):
#         super().breathe()
#         print("doing this underwater.")
#     def swim(self):
#         print("moving in water.")
#
#
# nemo = Fish()
# nemo.swim()
# nemo.breathe()


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r}({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


printer = Device("Printer", "USB")
print(printer)
printer.disconnect()


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer2 = Printer("Printer", "USB", 500)
printer2.print(20)
print(printer)
