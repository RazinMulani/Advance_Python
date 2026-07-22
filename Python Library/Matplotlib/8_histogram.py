# 8) Histogram in Matplotlib plt.hist()
# A Histogram is a graph used to show the distribution (frequency) of numerical data.

# Unlike a bar chart, a histogram groups continuous numerical values into intervals
#(called bins) and shows how many values fall into each interval.

# Basic Example:
'''
import matplotlib.pyplot as plt
import numpy as np

marks = np.array([45, 50, 52,55,60, 62, 65, 68, 70, 72, 75, 80, 82, 85, 90])
plt.title("Histogram")
plt.hist(marks)
plt.savefig("histogram.png")
plt.show()
'''

# Parameters In Histogram:
# x:Numerical data, bins:Number of intervals, color:Bar color, edgecolor:Border color,linewidth:Border thickness
# alpha:Transparency, density:Show probability density, histtype:Histogram style, label:Legend
# Example without bin
'''
import matplotlib.pyplot as plt
import numpy as np

marks = np.array([45,50,52,55,60,62,65,68,70,72,75,80,82,85,90])

plt.title("Histogram")
plt.hist(marks,
         color = "red",
         edgecolor="black",
         linewidth=3,
         alpha=0.8,
         density =True)
plt.savefig("without_bin.png")
plt.show()
'''
# Example with bin
'''
import matplotlib.pyplot as plt
import numpy as np

marks = np.array([45,50,52,55,60,62,65,68,70,72,75,80,82,85,90])

plt.title("Histogram")
plt.hist(marks,bins=5,
         color = "red",
         edgecolor="black",
         linewidth=3,
         alpha=0.8,
         density =True)
plt.savefig("with_bin.png")
plt.show()
'''

# Example Histtype: Change the style Of Histogram
# they are 4 types
# Syntax = histtype="bar"(bydefault)/"barstacked"/"step"/"stepfilled"
'''
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,2)

ax[0,0].hist([[45,50,52,55,60,62,65,68,70,72,75,80,82,85,90]],
                 bins=5,
                 color = "red",
                 edgecolor="black",
                 linewidth=3,
                 alpha=0.8,
                 density =True,
                 histtype="step")
ax[0,0].set_title("Step")

ax[0,1].hist([[45,50,52,55,60,62,65,68,70,72,75,80,82,85,90]],
                 bins=5,
                 color = "red",
                 edgecolor="black",
                 linewidth=3,
                 alpha=0.8,
                 density =True,
                 histtype="bar")
ax[0,1].set_title("Bar")

ax[1,0].hist([[45,50,52,55,60,62,65,68,70,72,75,80,82,85,90]],
                 bins=5,
                 color = "red",
                 edgecolor="black",
                 linewidth=3,
                 alpha=0.8,
                 density =True,
                 histtype="barstacked")
ax[1,0].set_title("Barstacked")

ax[1,1].hist([[45,50,52,55,60,62,65,68,70,72,75,80,82,85,90]],
                 bins=5,
                 color = "red",
                 edgecolor="black",
                 linewidth=3,
                 alpha=0.8,
                 density =True,
                 histtype="stepfilled")
ax[1,1].set_title("stepfilled")

plt.savefig("histtype.png")
plt.show()
'''
# Complete Example
'''
import matplotlib.pyplot as plt

marks = [45,50,52,55,60,62,65,68,70,72,75,80,82,85,90]

plt.figure(figsize=(8,5))

plt.hist(
    marks,
    bins=5,
    color="skyblue",
    edgecolor="black",
    linewidth=2,
    alpha=0.8,
    label="Student Marks"
)

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(axis="y")

plt.legend()
plt.savefig("histogram_example.png")

plt.show()
'''

# Histogram with Random Data

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data,
         bins=30,
         color="orange")
plt.savefig("random_data.png")
plt.show()


# Multiple Histograms(Without Using Subplots)
'''
import matplotlib.pyplot as plt
import numpy as np

math = np.random.normal(70, 10, 200)
science = np.random.normal(65, 8, 200)
history = np.random.normal(80, 6, 200)

plt.hist(math, bins=15, alpha=0.6, label="Math")
plt.hist(science, bins=15, alpha=0.6, label="Science")
plt.hist(history, bins=15, alpha=0.6, label="History")

plt.legend()
plt.savefig("Multiple_histogram.png")
plt.show()
'''












