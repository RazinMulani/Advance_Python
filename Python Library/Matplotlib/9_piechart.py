# 9) Pie Chart
# A Pie Chart is a circular graph used to represent parts of a whole (100%).
# It divides a circle into slices, where each slice represents a category's contribution to the total.

# Example:
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
plt.title("Example Of PieChart")
plt.pie(x)
plt.savefig("piechart.png")
plt.show()
'''

# Labels: Used to desplay the name of each slice
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])  
plt.title("Add Labels In Pie Chart")
plt.pie(x,labels=subjects)
plt.savefig("labels_pie.png")
plt.show()
'''

# autopct :Desplay The Percentage OF Each Slice
# syntax = autopct="%1.1f%%"
# % → Start formatting
# 1 → Minimum width
# .1 → One digit after the decimal point
# f → Floating-point number
# %% → Displays the % symbol
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])  
plt.title("Desplay The Percentage In Pie Chart")
plt.pie(x,labels=subjects,autopct="%1.1f%%")

plt.savefig("percentage_pie.png")
plt.show()
'''
# colors: Change The Color Of Each Slice
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Add Own Color In Pie Chart")
plt.pie(x,labels=subjects,autopct="%1.1f%%",colors=["red","green","blue","yellow"])
plt.savefig("Add_Colors.png")
plt.show()
'''
# explode=[0,0.2,0,0]:
# Separates one or more slices from the pie chart to highlight them.
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Slices in The Pie Chart")
plt.pie(x,
        labels=subjects,
        autopct="%1.1f%%",
        colors=["red","pink","black","green"],
        explode=[0,0.2,0,0])
plt.savefig("slices_pie.png")
plt.show()
'''

# shadow: Add a Shadow Below The Pie Chart
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Add Shadow in The Pie Chart")
plt.pie(x,
        labels=subjects,
        autopct="%1.1f%%",
        colors=["red","pink","black","green"],
        explode=[0,0,0.2,0],
        shadow=True)
plt.savefig("shadow_pie.png")
plt.show()
'''
# startangle:Rotate The Starting of The Pie Chart
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Rotate The Pie Chart")
plt.pie(x,
        labels=subjects,
        autopct="%1.1f%%",
        colors=["red","pink","black","green"],
        explode=[0,0,0.2,0],
        shadow=True,
        startangle=90)
plt.savefig("rotate_pie.png")
plt.show()
'''
# Radius : Change The Size Of The Pie Chart
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Change The Size of The Pie Chart")
plt.pie(x,
        labels=subjects,
        colors=["red","pink","black","green"],
        autopct="%1.1f%%",
        explode=[0,0,0.2,0],
        shadow=True,
        startangle=180,
        radius=1.5)
plt.savefig("change_size_pie.png")
plt.show()
'''
# CounterClock: Controls The Drowing Direction
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Change The Size of The Pie Chart")
plt.pie(x,
        labels=subjects,
        autopct="%1.1f%%",
        colors=["red","pink","black","green"],
        explode=[0,0,0.2,0],
        shadow=True,
        startangle=180,
        radius=0.5,
        counterclock=False)## bydefult True
plt.savefig("counterclock_pie.png")
plt.show()
'''

# wedgeprops: Customizes the appearance of slice borders.
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Customize the Apperance of the slice in The Pie Chart")
plt.pie(x,
        labels=subjects,
        autopct="%1.1f%%",
        colors=["red","pink","yellow","green"],
        explode=[0,0,0.2,0],
        shadow=True,
        counterclock=False,
        startangle=90,
        radius=1,
        wedgeprops={
            "edgecolor":"black",
            "linewidth":2}
        )

plt.savefig("add_wedgeprops_pie.png")
plt.show()
'''

# Textprops: Change The Apparance of labels and percentage
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Customize the Apperance of the slice in The Pie Chart")
plt.pie(x,
        labels=subjects,
        autopct="%1.1f%%",
        colors=["red","pink","yellow","green"],
        explode=[0,0,0.2,0],
        shadow=True,
        counterclock=False,
        radius=1.2,
        startangle=45,
        wedgeprops={
            "edgecolor":"black",
            "linewidth":2
            },
        textprops={
            "fontsize":12,
            "color":"blue"
            }
        )

plt.savefig("Change_text_apparance_pie.png")
plt.show()
'''

# pctdistance:control the position of the percentage text
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Customize the Apperance of the slice in The Pie Chart")
plt.pie(x,
        labels=subjects,
        autopct="%1.1f%%",
        colors=["red","pink","yellow","green"],
        explode=[0,0,0.2,0],
        shadow=True,
        counterclock=False,
        radius=0.8,
        startangle=45,
        wedgeprops={
            "edgecolor":"black",
            "linewidth":2
            },
        textprops={
            "fontsize":12,
            "color":"blue"
            },
        pctdistance=0.7
        )
plt.savefig("control_position_of_the_percentage.png")
plt.show()
'''
# labeldistance:Control The Distance of a labels
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.array([40,30,20,10])
subjects = np.array(["Math","Science","English","Hindi"])
plt.title("Customize the Apperance of the slice in The Pie Chart")
plt.pie(x,
        labels=subjects,
        labeldistance=1.2,
        autopct="%1.1f%%",
        pctdistance=0.7,
        colors=["red","pink","yellow","green"],
        explode=[0,0,0.2,0],
        shadow=True,
        counterclock=False,
        radius=1.2,
        startangle=45,
        wedgeprops={
            "edgecolor":"black",
            "linewidth":2
            },
        textprops={
            "fontsize":12,
            "color":"blue"
            }
        )
plt.savefig("control_position_of_the_label.png")
plt.show()
'''
# Complete Example
import matplotlib.pyplot as plt

marks = [40,30,20,10]
subjects = ["Math","Science","English","Hindi"]

plt.figure(figsize=(8,8))

plt.pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%",
    colors=["red","blue","green","yellow"],
    explode=[0,0.1,0,0],
    shadow=True,
    startangle=90,
    wedgeprops={
        "edgecolor":"black",
        "linewidth":2
    },
    textprops={
        "fontsize":11
    }
)

plt.title("Student Marks Distribution")
plt.legend(subjects)
plt.savefig("complete_example.png")
plt.show()

