# 2) Ploting "plt.plot()"

# Ploting Important Parameters

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
# MARKERFACECOLOR : Change the Inside Color Of Marker
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [3,4,1,7,2,5,6]

plt.plot(x,y,color="pink",linestyle=":",linewidth=5,marker='o',markersize=12,markerfacecolor="black")
plt.title("Add Marker Face Color")
plt.grid()
plt.savefig("marker_face_color.png")
plt.show()
'''

# MARKEREDGECOLOR : Change The MArker Edge Color
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [3,4,1,7,2,5,6]

plt.plot(x,y,color="purple",linestyle="-.",linewidth=5,marker="o",markersize=12,markerfacecolor="red",
         markeredgecolor="black")

plt.title("Add Marker Edge Color")
plt.grid()
plt.savefig("marker_edge_color.png")
plt.show()
'''

# MARKEREDGEWIDTH :  Change The Thickness Of Edge
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
         markeredgewidth=3)

plt.title("Add Marker Edge Width")
plt.grid()
plt.savefig("marker_edge_width.png")
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







