# LABEL in Matplotlib
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
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,10])
y = np.array([0,500])

plt.plot(x,y)
plt.title("Demo Line Graph")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.show()
'''
# X Label Properties
#Fontsize=change the size of label,color=change the color of label,
#fontwight=change the width of label (normal,bold),labelpad= Add Padding of the label
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,10])
y = np.array([0,500])

plt.plot(x,y)
plt.title("X-axis label properties Graph")
plt.xlabel("x-axis",color="red",fontsize=15,fontweight="bold",labelpad=15)
plt.ylabel("y-axis",color="red",fontsize=15,fontweight="bold",labelpad=15)

plt.savefig("Add_properties_in_xandy_label.png")
plt.show()
'''
# legend(): show label of top left inside the graph
# Display The Legend
'''
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,3])
y = np.array([0,3])

plt.plot(x,y,label="Boys")
plt.title("Demo Line Graph")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.legend()
plt.show()
'''

# legend() Properties
# 1) Change the legend Position(loc)


#loc="upper right"	Top-right (default)
'''
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="upper right") # bydefault

plt.savefig("upperright.png")
plt.show()
'''
#"upper left"	Top-left
'''
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="upper left") # bydefault

plt.savefig("upperleft.png")
plt.show()
'''
#"lower left"	Bottom-left
'''
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="lower left") # bydefault

plt.savefig("lowerleft.png")
plt.show()
'''
#"lower right"	Bottom-right
'''
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="lower right") # bydefault

plt.savefig("lowerright.png")
plt.show()
'''
#"center"	Center
'''
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="center") # bydefault

plt.savefig("center.png")
plt.show()'''
#"best"	Automatically chooses the best location
'''
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="best") # bydefault

plt.savefig("best.png")
plt.show()
'''

# 2) fontsize = change the font size
'''
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="best",fontsize=14) # bydefault

plt.savefig("legend_fontsize.png")
plt.show()
'''
# 3) title = take title for legend
'''
import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="best",fontsize=14,title="demo") # bydefault

plt.savefig("legend_title.png")
plt.show()
'''
# 4) frameon = False,, Remove legend border, bydefaoult it is True

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,15,30]

plt.plot(x,y,label="Sales")

plt.legend(loc="best",fontsize=14,title="demo",frameon = False) # bydefault

plt.savefig("legend_frameon.png")
plt.show()



