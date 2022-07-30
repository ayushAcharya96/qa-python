# # def func():
# #     global local_variable
# #     local_variable = 200
# #     global global_variable
# #     global_variable = 300
# #
# # func()
# # print(global_variable)
# # print(local_variable)
#
# def add(a, b):
#     pass
# def substract():
#     pass
# def multiply():
#     pass
# def divide():
#     pass
#
# class Math():
#     def add(self, a, b):
#         return a + b
#
#     def subtract(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         return a / b
#
# class Algebra(Math):
#     def factorize(self):
#         return 0
#     def simplify(self):
#         return 0
#
# class Geometry(Math):
#     def findAngle(self):
#         return 0
#     def findArea(self):
#         return 0
#
#
# geometry1 = Geometry()
# # geometry1.findArea()
# print(geometry1.add(2,4))

class Student:
    def __init__(self, name, age, batch):
        print("This is a constructor")
        self.name = name
        self.age = age
        self.batch = batch

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_batch(self):
        return self.batch

    def display(self):
        print(self.name, self.age, self.batch)


students = []
for student in range(3):
    name = input("Enter name")
    age = input("Enter age")
    batch = input("Enter batch")
    student = Student(name, age, batch)
    students.append(student)

batch_dict = {}
for student in students:
    if student.batch in batch_dict.keys():
        batch_dict[student.batch] = batch_dict[student.batch] + 1
    else:
        batch_dict[student.batch] = 1

print(batch_dict)