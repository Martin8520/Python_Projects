class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 100, 93, 78, 90))
student2 = Student("Mike", (99, 87, 93, 78, 90))
print(f"Student name: {student.name}\nStudent grades:{student.grades}\nGrades average:{student.average()}")
print(f"Student name: {student2.name}\nStudent grades:{student2.grades}\nGrades average:{student2.average()}")
