# Practice Question Of File Handling
# Q1. Student Record
# Create a Python program that asks for a student's name, age, and marks and saves the information into
# student.txt
'''
std_name = input("Enter Student Name: ")
std_age = int(input("Enter Age Of Student: "))
std_marks = float(input("Enter Students Marks"))

with open("student.txt","a") as file:
    file.write(f"Student Name: {std_name} | Student Age: {std_age} | Student Marks: {std_marks}\n")

print("Student Recorde Saved!")
'''
# Q2. Q2. Read Student Data
# Read student.txt and display all student information on the screen.
'''
with open("student.txt","r") as f:
    data  = f.read()
    print(data)
'''

# Q3. Daily Notes
# Create a program that takes a note from the user and appends it to notes.txt without deleting previous
# notes.
'''
note = input("Enter Your Notes: ")
with open("notes.txt","a") as f:
    f.write(note + "\n")

print("Note Saved Successfully!")
'''
# If you want Delete all Data From Text File Use "Pass" Keyword
'''
with open("notes.txt","w") as f:
    pass
print("All Data Delete successfully!")
'''
# Q4. Employee Details
# Ask for employee name, ID, and salary and save the details in employees.txt.
'''
name = input("Enter Employee Name: ")
ID = int(input("Enter Employee ID: "))
salary = float(input("Enter Employee Salary: "))

with open("employees.txt","a") as file:
    file.write(f"Employee Name: {name} | Employee ID: {ID} | Employee Salary: {salary}\n")

print("Save Data Successfully!")
'''
# Q5. Attendance System
# Create a program that asks:
# Enter student name:
# Enter attendance (Present/Absent):
# Save the result in attendance.txt.
'''
name = input("Enter Student Name: ")
status = input("Present/Absent :")

with open("attendance.txt","a") as f:
    f.write(f"{name} - {status}\n")
    
print("Save Data successfully!")
'''
# Q6. Search Student
# Read students.txt and ask the user for a student name.
# If the name exists, display:
# Student Found
# Otherwise:
# Student Not Found

student_name = input("Enter Search student Name: ")

with open("student.txt","r") as file:
    data = file.readline()

found = False

for line in data:
    if line.strip().lower() == student_name.strip().lower():
        found = True
        break

if found:
    print("Student Found Successfully!")
else:
    print("Student Not Found!")


