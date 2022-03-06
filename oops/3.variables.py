# instance variable -> object variable
# class variabe -> class variable

class Student:
    name = 'student name'
    age = 18

student1 = Student()

student1.gender = 'M'

print(student1.name)
print(student1.gender)

print(student1.__dict__)