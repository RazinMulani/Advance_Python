# Types OF Metplotlib:
# 1)pyplot 2)plotting 3)marker 4)line 5)labels 6)Grid 7)subplots 8)scatters 9)Bars
# 10)Histogram 11)piecharts

# 1) pyplot
# pyplot is a module inside a matplotlib library that provide simple function that creating graphs and chart

'''import matplotlib.pyplot as plt  # "plt" is a nickname of "matplotlib.pyplot"'''

#Example 1):-
#Draw a Simple graph
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y) # line graph function

plt.show() # desplay function
'''
# Example 2):-
#Draw a line in a diagram from position (0,0) to position (6,250):
'''
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()
'''

# ploting X and Y points
# plot():
# The plot() function is used to draw points(Markers) in a diagram.
# By default, The plot() function Drows a line from point to point.
# The funtion takes parameters for specifying point in the diagram
# Parameter 1 is an array containing the points on the x-axis.
# Parameter 2 is an array containing the points on the y-axis.

# if We need to plot a line from (1,3) to (8,10),
# We have to pass two arrays [1,8] and [3,10] to the plot function

#Example:-
#Draw a line in a diagram from position (1, 3) to position (8, 10):
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,8])
y = np.array([3,10])

plt.plot(x,y)
plt.show()
'''

# figure(): syntax: plt.figure(figsize=(width,height))
# figsize determines the size of the graph (figure) that Matplotlib creates.
# Create  A new figure.
'''
import matplotlib.pyplot as plt

plt.figure(figsize=(8,7))

x = [1,2,3]
y = [4,5,6]

plt.plot(x,y)
plt.show()
'''

# title(): syntax: plt.title("Students Graph")
# Add a title:
'''
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.plot([1,2,3],[10,20,30])
plt.title("Students Marks")
plt.show()
'''
# xlabel(): syntax: plt.xlabel("X Points Name")
# Add Label X
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5))

x = np.array([0,10])
y = np.array([0,500])

plt.plot(x,y)
plt.title("Demo Line Graph")
plt.xlabel("X-axis Label")

plt.show()
'''
# ylabel(): syntax: plt.ylabel("Y Points Name")
# add Label Y

import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,10])
y = np.array([0,500])

plt.plot(x,y)
plt.title("Demo Line Graph")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.show()





