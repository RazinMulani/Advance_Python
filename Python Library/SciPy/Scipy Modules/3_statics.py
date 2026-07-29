#scipy.stats	Statistics

# DEFINITION: scipy.stats is scipy module that provides function for discriptive Statistics, Probablity
# Distribution, Stastical Tests, and Random Variable Analysis.

#Why do we use scipy.stats?

# Imagine you have marks of 10,000 students.
# Finding the average manually would take a long time.
# SciPy can calculate it in milliseconds.
# Similarly, it can calculate: Mean, Median, Mode, Variance, Standard deviation, Probability, Correlation
# Statistical tests

# They are tow ways to import module
# 1) Import The Complete Module
'''from scipy import stats'''

# 2) Import a Spacific Module
'''from scipy.stats import tmean'''

# Types Of Statistics:
# Statistics mainly Divided into Two Categories.

# 1) Descriptive Statistics(summarizes existing data.): Mean, Median, Mode, Variance, Standard Deviation
# MEAN(Average): The mean is the sum of all values divided by the total number of values.
# formula: sum of all values/Number of values
'''
from scipy.stats import tmean

marks = [55,35,78,90,67]

result = tmean(marks)
print(result)
'''

# MEDIAN: The median is the middle value after aranging the data in ascending or descending order.
'''
from scipy import stats

marks = list(map(int, input("Enter The Number With space: ").split()))
result = stats.median_abs_deviation(marks)
print(result) # 11.0
'''
# or  Using numpy(acurate)
'''
import numpy as np

marks = list(map(int, input("Enter The Numbers with Space: ").split()))
result = np.median(marks)
print(result) # 78.0
'''

# MODE: The mode is the value that appears most frequently in a dataset.
'''
from scipy import stats

n = int(input("How many number You want? "))

marks = []

for i in range(n):
    mark = int(input(f"Enter The Marks{i+1}"))
    marks.append(mark)

result = stats.mode(marks)
print(result)
'''
# VARIANCE: Variance measures how far the data values are spread from the mean.
# A small variance means the values are close together.
# A large variance means the values are spread out.
'''
from scipy import stats

n = int(input("How Many Students Are Hear? "))

marks = []

for i in range(n):
    mark = int(input(f"Enter Marks{i+1}: "))
    marks.append(mark)

result = stats.tvar(marks)
print(result)
'''
# STANDARD DEVIATION: Standard deviation measures how much the values differ from the average.
# It is the squareroot of the variance

from scipy import stats

marks = [70,80,90,60,100]

print(stats.tstd(marks))
# 2) Inferential Statistics(helps us make predictions or conclusions about a larger population using a
# sample.): Hypothesis Testing, Confidence Interval, Regression, Correlation
