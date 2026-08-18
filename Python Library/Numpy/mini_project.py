# Mini Project In Numpy

import numpy as np

marks = np.array([
    [78, 85, 69, 90],
    [65, 72, 80, 75],
    [92, 88, 95, 90],
    [45, 55, 48, 60],
    [81, 79, 85, 88]
    ])
print("Student Marks: \n",marks)

# Basic Information
# Display: Number of Students:, Number of Subjects:, Array Dimensions:, Total Elements:, Data Type:

print("\nNumber of Students: ",marks.shape[0])
print("Number of Subjects: ",marks.shape[1])
print("Array Dimension: ",marks.ndim)
print("Total Elements: ",marks.size)
print("Shape of Array: ",marks.shape)
print("Data Type Array: ",marks.dtype)

# Q2. Total Marks of Each Student
# Calculate the total marks for every student.
print("\nTotal Marks Of Each Students: ")
total_marks = np.sum(marks, axis = 1)
num = 1
for data in total_marks:
    print(f"Student {num}:",data)
    num += 1

# Q3. Average Marks
# Calculate the average marks of every student.

print("\nAverage Marks Of Each Students: ")
avg_marks = np.mean(marks, axis = 1)
num = 1
for data in avg_marks:
    print(f"Student {num}: ",data)
    num += 1

# Q4. Highest and Lowest Marks
# Find: Highest mark in the entire array, Lowest mark in the entire array

print("\nHighest and Lowest Marks in the entire array: ")
hig_marks = np.max(marks)
print("Heighest Marks in Entire Array: ",hig_marks)

min_marks = np.min(marks)
print("Lowest Marks In Entire Array: ",min_marks)

# Q5. Subject-wise Analysis
# Find the highest marks in each subject.

print("\nHighest and Lowest Marks of Each Subject: ")

hig_sub = np.max(marks, axis = 0)

sub = ["Python","NumPY","Pandas","Java"]
print("Highest marks of Each Subject: ")
for data in range(len(sub)):
    print(sub[data],":", hig_sub[data])


low_sub = np.min(marks, axis = 0)

sub = ["Python","NumPY","Pandas","Java"]
print("\nLowest marks of Each Subject: ")
for data in range(len(sub)):
    print(sub[data],":", low_sub[data])
    
    
    
    






