# Pandas
#Creating a simple pandas DataFrame(user define)

import pandas as pd
#print(pd.__version__)


# Creating Data Frame Using a Dictionary
data = {"name":["Razin","Sami","Shabnoor"],
        "age":[22,20,24],
        "city":["Mahabaleshwar","Mumbai","Pune"]}
df = pd.DataFrame(data)
print(df)
'''
#View Data Frame
print("1st person")
print(df.loc[0])

print("2nd person")
print(df.loc[1])

print("3rd person")
print(df.loc[2])

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
'''





