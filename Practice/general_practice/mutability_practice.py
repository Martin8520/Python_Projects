# a = "hello"
# print(a)
# b = 8555
# a += " world"
# print(a)
# print(b)
from typing import List, Optional


class Student:
    # def __init__(self, name: str, grades: List[int] = []):  # This is bad
    def __init__(self, name: str, grades: Optional[List[int]] = None):  # This is good

        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


ralf = Student("Ralf")
bob = Student("Bob")
bob.take_exam(90)
print(bob.grades)
print(ralf.grades)
