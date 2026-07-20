# Line In Matplotlib
# COLOR
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,5))
x = np.array([1,2,3])
y = np.array([4,5,6])

plt.plot(x,y,color="red")
plt.grid()
plt.savefig("chnage_the_line_color.png")
plt.show()
'''
# LINESTYLE: Change The Linestyle
'''
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(2,2,figsize=(9,6))
ax[0,0].plot([1,2,3,4,5,6,7],[1,2,3,4,5,6,7],color="yellow",linestyle="--",label="Data 1")
ax[0,0].set_title("Dashed")
ax[0,0].set_xlabel("x-axis")
ax[0,0].set_ylabel("y-axis")
ax[0,0].grid(True)
ax[0,0].legend()

ax[0,1].plot([1,2,3,4,5,6,7],[1,2,3,4,5,6,7],color="red",linestyle="-",label="Data 2")
ax[0,1].set_title("Solid")
ax[0,1].set_xlabel("x-axis")
ax[0,1].set_ylabel("y-axis")
ax[0,1].grid(True)
ax[0,1].legend()

ax[1,0].plot([1,2,3,4,5,6,7],[1,2,3,4,5,6,7],color="blue",linestyle=":",label="Data 3")
ax[1,0].set_title("Dotted")
ax[1,0].set_xlabel("x-axis")
ax[1,0].set_ylabel("y-axis")
ax[1,0].grid(True)
ax[1,0].legend()

ax[1,1].plot([1,2,3,4,5,6,7],[1,2,3,4,5,6,7],color="cyan",linestyle="-.",label="Data 4")
ax[1,1].set_title("Dash-Dot")
ax[1,1].set_xlabel("x-axis")
ax[1,1].set_ylabel("y-axis")
ax[1,1].grid(True)
ax[1,1].legend()

#they are four types "-" solid is bydefault linestyle
plt.savefig("Linestyle_change.png")
plt.show()
'''

# LINEWIDTH: Change The Thickness of the line
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [3,4,1,7,2,5,6]
plt.plot(x,y,color="green",linestyle="-.",linewidth=5)
plt.savefig("linewidth.png")
plt.show()
'''
# MARKERS and MARKERSIZE: Display Symbols at every data point and increase the size
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [3,4,1,7,2,5,6]

plt.plot(x,y,color="orange",linestyle="--",linewidth=5,marker="o",markersize=12)
plt.title("Add Marker And Change MArker Size")
plt.grid()
plt.savefig("marker.png")
plt.show()
'''
# LABEL: Use to create a lagend
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [3,4,1,7,2,5,6]

plt.plot(x,y,
         color="green",
         linestyle="-",
         linewidth=5,
         marker='o',
         markersize=12,
         markerfacecolor="black",
         markeredgecolor="red",
         markeredgewidth=3,
         label="Data")

plt.title("Add Label")
plt.grid()
plt.legend()
plt.savefig("label.png")
plt.show()
'''
# ALPHA: Control Transparancy "value range from 0 to 1"
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [3,4,1,7,2,5,6]

plt.plot(x,y,
         color="red",
         linestyle="--",
         linewidth=5,
         marker = "o",
         markerfacecolor="green",
         markersize=12,
         markeredgecolor="black",
         markeredgewidth=2,
         label="data",
         alpha = 0.5)
# alpha value 0 = Completly transparent,
# alpha value 0.5 = Semi-transparent,
# alpha value 1 = Fully Visibal

plt.title("Add Transparency")
plt.grid()
plt.savefig("alpha.png")
plt.show()
'''
# Complete Example
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [20,40,35,50,45]

plt.plot(
    x,
    y,
    marker="o",
    markersize=12,
    markerfacecolor="yellow",
    markeredgecolor="red",
    markeredgewidth=2,
    color="blue",
    linewidth=3
)

plt.title("Student Performance")
plt.xlabel("Tests")
plt.ylabel("Marks")
plt.grid(True)

plt.show()
