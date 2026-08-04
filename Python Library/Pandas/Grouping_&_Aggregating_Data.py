# Grouping And Aggregating Data
# In Python, Grouping and Aggregating data is most commonly done with pandas
# --> Grouping menas dividing data into group based on one or more columns.
# --> Aggregation means performing calculation (like sum,average, min, max, count, etc.

# 1) Grouping Data in DataFrame
# --> This method follows a split-apply-combine process:
# 1) split: Split the data into groups
# 2) Apply: Apply some Calculation like sum, Average etc.
# 3) Combine: Combine the result into a new table.

import pandas as pd
print("Original DataFrame")
data = {"Item":['Cake','Cake','Bread','Pasty','Cake'],
        "Flavor":['Chocolate','Vanilla','Whole Wheat','Strawberry','Chocolate'],
        "Price":[250,220,80,120,250]}
df = pd.DataFrame(data)
print(df)

print('\n=====================================================\n')

#Grouping Data By One Column Using "groupby()"
print("Grouping Data By One Column Using 'groupby()'.")

print(df.groupby('Item')['Price'].sum())
print('\n=====================================================\n')

# Grouping by Multiple Columns:
print("Grouping Multiple Columns:")

print(df.groupby(['Item','Flavor'])['Price'].sum())

print('\n=====================================================\n')

# 2) Aggregation("agg()") Data In DataFrame:
print("Aggregation Data In DataFrame.")

# Crating Sample DataSet:
data = {"Maths":[9,8,7],
        "English":[4,10,6],
        "Science":[8,7,8],
        "History":[9,6,5]}

df = pd.DataFrame(data)
print(df)

print('\n=====================================================\n')
# Function:
# 1) sum() : Compute Sum Of Column Values
print("Summing Up All Values(sum())")

print(df.sum())
print('\n=====================================================\n')
# 2) min() : Compute Min Of Column Values
print("Min Valus")
print(df.min())

print('\n=====================================================\n')
# 3) max() : Compute Max Of Column Values

print("Max Values")
print(df.max())

print('\n=====================================================\n')
# 4) mean(): Compute Mean Of Column

print("Mean Of Column")
print(df.mean())

print('\n=====================================================\n')
# 5) size(): Compute Column Sizes

print("Colum Sizes")
print(df.size)

print('\n=====================================================\n')
# 6) describe(): Generate Descriptive Statistics

print("Describe A Summary")
print(df.describe())

print('\n=====================================================\n')
# 7) first(): Compute First Of Group Values

print("Compute First Of Group Values")
print(df.groupby(['Maths']).first())

print('\n=====================================================\n')
# 8) last(): Compute Last Of Group Values

print("Compute First Of Group Values")
print(df.groupby(['History']).last())

print('\n=====================================================\n')
# 9) count(): Compute Count Of Column Values

print("Count Of Column Values")
print(df.count())

print('\n=====================================================\n')
# 10) std(): Compute Standard Deviation of Column

print("Standar Deviation Of Column")
print(df.std())

print('\n=====================================================\n')
# 11) var(): Compute Variance Of Column

print("Variance Of Columns")
print(df.var())

## Applying Multiple Agregation at Once(agg())

print('\n=====================================================\n')
print("Using Multiple Aggregation at Once'agg()'.")
print(df.agg(['sum','min','max']))




