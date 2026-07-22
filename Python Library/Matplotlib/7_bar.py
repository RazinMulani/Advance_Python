# 7) BAR Chart(plt.bar())
# A Bar Chart Is Used To Compare Values Between Different Categaries Using Rectangular Bars.
# The Heights of each bar repersents each values.

# Types Of Bar Chart

# 1) Verical Bar Chart (plt.bar())
# 2) Horizontal Bar Chart (plt.barh())

# plt.bar(): Verical Bar Chart
# Syntax: plt.bar(x,height)

#Example:
'''
import matplotlib.pyplot as plt


students = ["Razin","Sami","Asjad","Alam","Mohsin"]
marks = [75,60,45,80,55]
plt.ylim(100)
plt.bar(students,marks)

plt.show()
'''
# COLOR(Also Add Different Color To Each Bar), WIDTH,EDGECOLOR, LINEWIDTH, ALPHA, LABEL

import matplotlib.pyplot as plt

students = ["Razin","Sami","Asjad","Alam","Mohsin"]
marks = [75,60,45,80,55]

colors=["red","yellow","blue","black","green"]
plt.bar(students,marks,
        color=colors,
        width=0.5,
        edgecolor="pink",
        linewidth=3,
        alpha=0.6,
        label="bar chart")

plt.legend(loc="best",fontsize=10,title="demo")
plt.grid(True)
plt.savefig("all_properties_of_bar.png")
plt.show()


# 2) Horizontal Bar Char (plt.barh()) get same properties(like,color,width,edgewidth,linewidth,alpha,label)
# Syntax: plt.barh(y, width)
'''
import matplotlib.pyplot as plt


students = ["Razin","Sami","Asjad","Alam","Mohsin"]
marks = [75,60,45,80,55]
plt.xlim(100)
plt.barh(students,marks)
plt.savefig("horizontal1_bar.png")

plt.show()
'''


