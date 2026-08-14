# Numpy

'''
import numpy as np
print("Version:",np.__version__)

a = [10,20,30,40]
b = np.array(a)

print(b)
'''
'''
import numpy
a = [10,20,30,40]
b = numpy.array(a)
print(b)
'''
'''
import numpy as np
a = [10,20,30,40,50,60,70,80,90,100]
b = numpy.array(a)

print(b)
'''
#
'''
import numpy as np

a =[]
n = int(input("Enter The Element: "))
for i in range(n):
    value = int(input("Enter Value:"))
    a.append(value)
myarray = np.array(a)
'''

#
'''
import numpy as np
a = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
             )
print(a)
print("Total Dimension:",a.ndim)
print("Shape:",a.shape)
'''
# Slicing 2-D
import numpy
a = numpy.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])
print(a[:2])
print(a[:3,1:3])
