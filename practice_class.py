# Practice Question For Class

# Q1. Student Class
# Create a class Student with:
# name, age, course
# Create an object and print all three values.

print("Meyhod 1: Using Constructor:")
class student:
    def __init__(self):
        self.name = "Razin"
        self.age = 22
        self.course = "Computer Engineering"
    def display(self):
        print("Name Of Student:",self.name)
        print("Age Of Student:",self.age)
        print("Name Of Course:",self.course)

s1 = student()
s1.display()

# Without Construcotr
print("Method 2: Without Constructor:")
class Students:
    def display(self):
        print("Name Of Student:",self.name)
        print("Age Of Student:",self.age)
        print("Name Of Course:",self.course)

s1 = Students()

s1.name = "Sami"
s1.age = 20
s1.course = "BCS"

s1.display()
