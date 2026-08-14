# Practice Question Of NumPy

import numpy as np

# Q1. Create an Array
# Create a NumPy array containing:

arr = np.array([10,20,30,40,50,60,70])
print(arr)

# Q2. Array Properties
# Print: Number of dimensions, Number of elements, Data type, Shape
print("\nNumber OF Dimension:",arr.ndim)
print("\nNumber OF Element:",arr.size)
print("\nShape:",arr.shape)
print("\nData Type:",arr.dtype)


# Q3. Access Elements
# Print: First element, Last element, Third element

print("\nFirst Element Of an Array: ",arr[0])
print("\nLast Element Of an Array: ",arr[-1])
print("\nThired Element Of an Array: ",arr[2])

# Q4. Slicing
# Print: First 3 elements, Last 3 elements, Elements from index 2 to 5, Every second element

print("\nGet First 3 Elements:",arr[0:3])
print("\nGet Last 3 Elements:",arr[-3:])
print("\nGet Elements from index 2 to 5:",arr[2:6])
print("\nGet Every second element:",arr[::2])

# Q5. Arithmetic Operations
# Print: Addition, Subtraction, Multiplication, Division

a = np.array([10,20,30,40])
b = np.array([2,4,5,8])

add = a + b
print("\nAddition Of A & B: ",add)

sub = a - b
print("\nSubtraction Of A & B: ",sub)

mult = a * b
print("\nmultiplication Of A & B: ",mult)

div = a / b
print("\nDivisionn Of A & B: ",div)

# Q6. Find Maximum and Minimum

print("\nMaximum Element of an Array: ",arr.max())
print("\nMinimum Number Of an Array: ",arr.min())

# Q7. Total marks, Average marks

marks = np.array([78,85,69,90,88])
total_marks = marks.sum() # OR np.sum(marks)
print("\nTotal Marks Of An Array: ",total_marks)
avg = marks.mean() # OR np.mean(marks)
print("\nAverage Marks Of An Array: ",avg)

# Q8. Find The Index Position of Heighest Value(Maximum)
arr1 = np.array([25, 75, 45, 95, 60])
mx = np.argmax(arr1)
print("\nIndex Position of Heighest Value(Maximum):",mx)
#o/p: Index Position of Heighest Value(Maximum): 3

# Q9. Find Position of Minimum
mn = np.argmin(arr1)
print("\nIndex Position of Lowest Value(Minimum):",mn)

# Q10. Create a Matrix
# Create this matrix using NumPy:
# given: 10 20 30
#        40 50 60
#        70 80 90
# Print: Print:Shape, Dimensions, Number of elements

mrx = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ])
print("nMAtrix: \n",mrx)
print("\nShape Of Matrix: ",mrx.shape)
print("\nDimension Of Matrix: ",mrx.ndim)
print("\nNumber Of Element:  ",mrx.size)

# Q11. Access Matrix Elements
# Using the above matrix, print:50, 70, First row, Last row, Second column

print("\nPrint '50': ",mrx[1,1])
print("\nPrint '70': ",mrx[2,0])
print("\nFirst Row: ",mrx[0])
print("Last Row: ",mrx[2])
print("Second Column:",mrx[:,1])

# Q12. Matrix Slicing
# Print: First two rows, Last two columns, Middle 2×2 matrix

print("\nFirst two rows: \n",mrx[1:])
print("\nLast two column: \n",mrx[:,-2:])
print("\nMiddle 2x2 matrix: \n",mrx[0:2, 1:3])

# Q13. Row-wise Sum    
# Given:- arr = np.array([
#    [10, 20, 30],
#    [40, 50, 60],
#    [70, 80, 90]
#])

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\nMatrix: \n",arr2)
rows = np.sum(arr2, axis=1)
print("\nAddition Of The Rows:",rows)

# Q14. Column-wise Sum 
# Using the same matrix, find the sum of each column.

columns = np.sum(arr2, axis=0)
print("\nAddition Of the Column",columns)

# Q15. Row-wise Average
# Find the average of every row

avg_row = np.mean(arr2, axis=1)
print("\nAverage Of the Rows:",avg_row)

# Q16. Column-wise Maximum
# Find the maximum value from each column.

col_max = np.max(arr2, axis = 1)
print("\nMaximum Value From Each Column:",col_max)

# Q17. Find Numbers Greater Than 50
arr3 = np.array([10, 65, 30, 85, 45, 90, 25])
for num in arr3:
    if num >= 50:
        print("Greater Than 50:\n",num)

# without using loop

result = arr3[arr3 > 50]
print("\n       OR       \n")
print("Grater Than 50 Number in an array:\n",result)


# Q18. Find Even Numbers
# Using the same array, print only even numbers.

for even in arr3:
    if even % 2 == 0:
        print("Even:",even)

print("\n       OR       \n")
result1 = arr3[arr3 % 2 == 0]
print("Even Number in An Array:\n",result1)

# Q19. Find Odd Numbers
# Print only odd numbers.

for odd  in arr3:
    if odd % 2 != 0:
        print("Odd Number in an Array: ",odd)
        
print("\n       OR       \n")
result3 = arr3[arr3 % 2 != 0]
print("Odd Number in an Array: ",result3)

# 20. Marks Filtering
#Print: Students who passed (>= 40), Students who failed (< 40), Students who scored >= 80

std_marks = np.array([35, 67, 89, 45, 92, 28, 76, 55])
for mark in std_marks:
    if mark >= 40 and mark <= 79:
        print("Student Is Passe!",mark)
    elif mark >= 80 and mark <= 100:
        print("Topper In The Class!",mark)
    elif mark <= 40:
        print("Student Is Failed!",mark)
    else:
        print("Enter Valid Marks!",mark)


# Q21. Pass/Fail
# Use np.where() to convert marks into:
print("\nUsing where method: ")
marks = np.array([35, 67, 89, 45, 92, 28])
resu = np.where(marks >= 40 , "Pass","Faile")
print("Pass/Faile:",resu)


# Positive/Negative
# Use np.where() to print:
print("\nFind Positive And Negative Number:")
num = np.array([-10, 20, -5, 30, -15, 40])
PN = np.where(num >= 0 , "p+ve","N-ve")
print("Positive/Negative",PN)


# Q23. Replace Values
# Replace every value greater than 50 with 0 using np.where().
print("\nReplace above 50 into 0:")
replace = np.array([10, 25, 50, 75, 100])
rplc = np.where(replace > 50, 0, replace)
print(rplc)

#Q24. Student Marks Analyzer
# Given: marks = np.array([
#   [78, 85, 69],
#   [65, 72, 80],
#   [92, 88, 95],
#   [45, 55, 48],
#   [81, 79, 85]
#])

# Find:

marks = np.array([
    [78, 85, 69],
    [65, 72, 80],
    [92, 88, 95],
    [45, 55, 48],
    [81, 79, 85]
    ])

print(marks)
# Total marks of each student
total_mark = np.sum(marks, axis = 1)
print("\nTotal Marks Of Each Students:",total_mark)

# Average marks of each student
avg_mark = np.mean(marks, axis = 1)
print("\nTotal Marks Of Each Students:",avg_mark)

# Highest mark
hig_mark = np.max(marks)
print("\nHighest Marks:",hig_mark)

# Lowest mark
low_mark = np.min(marks)
print("\nLowest Marks:",low_mark)

# Highest mark in each subject
hig_mark_sub = np.max(marks, axis = 0)
print("\nHighest Mark in Each Subject:",hig_mark_sub)

# Average of each subject
avg_sub = np.mean(marks, axis = 0)
print("\nAverage of Each Subject:",avg_sub)

# Student with highest total
total_std = np.argmax(total_mark)+1
print("\nStudent With Highest Total:",total_std)

# Students with average >= 80
std_avg = np.where(avg_mark >= 80)[0]+1
print("\nStudents with average:",std_avg)

# Pass/fail status
pas_fail = np.where(avg_mark >= 40 ,"Pass","Faile")
print("\nPass/Fail:",pas_fail)
