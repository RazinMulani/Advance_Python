# Pandas
#Creating a simple pandas DataFrame(user define)

import pandas as pd
#print(pd.__version__)

# series

# 1) from list
'''
s = pd.Series([10,20,30])
print(s)
'''
# 2) add indexing
'''
s1 = pd.Series([10,20,30],index=['a','b','c'])
print(s1)
'''
# 3) from dictionary
'''
d = {'a':1,'b':2,'c':3}
s = pd.Series(d)
print(s)
'''
# 4) using Numpy array
'''
import numpy as np
arr = np.array([10,20,30])
s = pd.Series(arr)
print(s)
'''
# Creating Data Frame Using a Dictionary
'''
data = {"name":["Razin","Sami","Shabnoor"],
        "age":[22,20,24],
        "city":["Mahabaleshwar","Mumbai","Pune"]}
df = pd.DataFrame(data)
print(df)
'''
# Creating Data using List
data = [
    ["Razin",22,"Pune"],
    ["Sami",20,"Mahabi"],
    ["Alam",23,"Mumbai"]
    ]
df = pd.DataFrame(data,columns=["name","age","city"])
print(df)
#View Data Frame
'''
print("1st person")
print(df.loc[0])

print("2nd person")
print(df.loc[1])

print("3rd person")
print(df.loc[2])
'''
# Named Index:
# With The Index Argument, You Can Name Your Own Indexes.
print("Can you take your own name of index!")
df = pd.DataFrame(data, index = ["Value1","Value2","Value3"])
#print(df)

# Located Named Index:
# Use the named index in the loc attribute to return the specified row(s)
df = pd.DataFrame(data, index = ["Value1","Value2","Value3"])
print("Find Value Using Given Index Named")
print(df.loc["Value1"])
print(df.loc["Value2"])
print(df.loc["Value3"])






