# 6) Scatter Plots
# A Scatter Plots is a graph that desplays individual data point without connecting them with lines.
# Each Point represents one (x,y)cordinate
# uses: Show the relationship between two vaiables, Find Pattern or trends, Detect Outliers(Unusual values),
# Comapare Datasets

# Syntax: plt.scatter(x-axis,y-axis)
# Example:
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,1,3,5,4]

plt.title("Scatter Plots")
plt.scatter(x,y,marker="*")

plt.savefig("scatter_plots.png")
plt.show()
'''

# Properties Of Scatter Plots
# color or c
# C
'''
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [20,10,50,30,40]

plt.title("Add Color In Scatter Plots(using C)")
plt.scatter(x,y,c="red")
plt.savefig("add_color_in_scatter.png")
plt.show()
'''
# use COLOR
'''
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [20,10,50,30,40]

plt.title("Add Color In Scatter Plots(using COLOR)")
plt.scatter(x,y,color="blue")
plt.savefig("add_color_in_scatter_using_color.png")
plt.show()
'''
# Use Multiple Colors
'''
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [50,20,40,10,30]

plt.title("Add Multiple Color In Scatter Plots")
colors = ["red","green","blue","orange","pink"]
plt.scatter(x,y,c=colors)
plt.savefig("add_multiple_color_scatter.png")
plt.show()
'''
# s(size)
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [50,20,40,10,30]
plt.title("Change Size Of Scatter Plots")
plt.scatter(x,y,c="green", s=100)
plt.savefig("Change_size_of_scatter.png")
plt.show()
'''

# Add different size of each point
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [50,20,40,10,30]

colors=["red","green","yellow","blue","black"]
sizes = [50,100,150,200,250]

plt.scatter(x,y, c = colors, s=sizes)
plt.savefig("change_sizes_of_scatter.png")
plt.show()
'''
# marker
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,1,3,5,4]

plt.title("Scatter Plots")
colors=["red","green","yellow","blue","black"]
sizes = [50,200,150,100,250]

plt.scatter(x,y,marker="^", c = colors, s = sizes)

plt.savefig("change_marker_scatter.png")
plt.show()
'''
# alpha(transparancy)
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,1,3,5,4]

plt.title("Scatter Plots")
plt.title("Scatter Plots")
colors=["red","green","yellow","blue","black"]
sizes = [50,200,150,100,250]
plt.scatter(x,y,marker="*",c=colors,s=sizes,alpha=0.5)

plt.savefig("alpha_scatter.png")
plt.show()
'''

# label
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [50,20,40,10,30]
plt.title("Add Label In Scatter Graph")

colors=["red","green","yellow","blue","black"]
sizes = [50,200,150,100,250]

plt.scatter(x,y,c=colors,s=sizes, marker="s",label="demo",alpha=0.8)
plt.legend(loc="best",frameon=True,fontsize=12,title="scatter")

plt.savefig("add_label_scatter.png")
plt.show()
'''

# Complete Example:
'''
import matplotlib.pyplot as plt

x = [1,2,3,4,5]

y = [10,20,15,30,25]

plt.figure(figsize=(8,5))

plt.scatter(
    x,
    y,
    color="red",
    s=150,
    marker="*",
    alpha=0.8,
    label="Sales"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(True)

plt.legend()

plt.savefig("Complet_Example_Scatter.png")

plt.show()
'''
# Example Scatter Subplots
'''
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = [1,2,3,4,5]
y = [10,20,15,30,25]

ax.scatter(
    x,
    y,
    color="green"
    )

ax.set_title("Subplots in Scatter")
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")

plt.savefig("Subplots_in_Scatter.png")
plt.show()
'''
