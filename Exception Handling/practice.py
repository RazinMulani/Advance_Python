# Practice Example Of Exception Handling:
# 1. Basic try-except
# Question: Take two numbers from the user and divide them. Handle the error if the user enters 0 as the
# denominator.
'''
try:
    a = int(input("Enter The VAlue Of A: "))
    b = int(input("Enter The Value Of B: "))

    c = a/b
    print("Division of A & B: ",c)
    
except ZeroDivisionError :
    print("Zero Division Error Occured!")
'''
# 2. Handling Invalid Input
# Question: Ask the user to enter their age. If they enter text instead of a number, handle the exception.
'''
try:
    age = int(input("Enter The Age Of User: "))
    print("Age Of User:",age)
except ValueError as v:
    print("Error: Please Enter A Valid Number",v)
'''
# Question: Create a program that takes two numbers and divides them. Handle both:
# Invalid input
# Division by zero
'''
try:
    x = int(input("Enter Value Of X: "))
    y = int(input("Enter Value Of Y: "))

    result = x/y
    print("X divided By Y = ",result)

except ZeroDivisionError as e:
    print("Error",e)

except ValueError as v:
    print("Error",v)
'''

# Q4) Use try-except-else
'''
try:
    num = int(input("Enter Number: "))
    result = 100/num

except ValueError as v:
    print("Error",v)

except ZeroDivisionError as e:
    print("Error",e)

else:
    print("Result: ",result)
'''

# Q5) try-except-finally
# Real-life example: File handling
'''
try:
    f = open("data.txt","r")
    data = f.read()
    print(data)

except FileNotFoundError as e:
    print("File Does Not Exist", e)

finally:
    print("Program Completed...")

'''
# Create a calculator that handles:
# ValueError
# ZeroDivisionError
# +, -, *, /
'''
try:
    x = int(input("Enter Value Of X: "))
    y = int(input("Enter Value Of Y: "))

    add = x + y
    sub = x - y
    mult = x * y
    div = x / y

    print(add)
    print(sub)
    print(mult)
    print(div)

except ValueError as e:
    print("Error", e)

except ZeroDivisionError as z:
    print("Error", z)
    
'''
# Practice 2
# Create a program that asks for an index number and accesses this list:

# students = ["Rahul", "Amit", "Rohit", "Sneha", "Priya"]

try:
    students = ["Rahul", "Amit", "Rohit", "Sneha", "Priya"]

    index = int(input("Enter The Value of Index: "))
    print("Student: ",students[index])

except IndexError:
    print("Error: Invalid Index")

except ValueError:
    print("Error: Please Enter A Number")




















