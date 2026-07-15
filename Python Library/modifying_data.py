# Modifiying Data In DataFrame:

# --> Renaming column or row labels
#Example:
# The rename() method in Pandas allows renaming one or more columns or row labels
# To rename a column of a data frame
import pandas as pd
'''
print("Rename the column of a DataFrame:")
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
print("Original DataFrame")
print(df.to_string())

df = df.rename(columns={"A":"aa","B":"bb"})
print("Modified DataFrame")
print(df.to_string())

print("\n=======================================================\n")

print("Rename The Row Labels in The DataFarame:")
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]},index=["x","y","z"])
print("Original DataFrame")
print(df)

df = df.rename(index={"x":"r1","y":"r2","z":"r3"})
print(df.to_string())

print("\n=======================================================\n")

# --> Adding or Inserting New Column
# Additionally, You can use "DataFrame.insert()" method to insert a new column at a specific position

# Create DataFrame
df = pd.DataFrame({"I":["A","B","C"],"II":["D","E","F"]})
# Add a new column 'III' with values
df["III"]=["G","H","I"]

# Insert a new column "D" at postion 1
df.insert(1,"IV",["J","K","L"])
# Display Updated DataFrame

print("DataFarame After inserting column 'IV' at postion 1.")
print(df.to_string())

# Displaye updated DataFrame
print("DataFrame after adding a new column 'IV'.")
print(df)

print("\n=======================================================\n")

# --> Updating or Replacing existing column values
# DataFrame.replace() method is use to replace specific values within a column of a DataFrame:

print("Updating or Replaceing Exicsting Column Values:")
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})

#Display the Input DataFrame
print("Original Data Frame:",df,sep='\n')

# Replace the content
df.replace({"A":1,"B":6},100,inplace = True)
print("DataFrame after replacing column 'A':")
print(df)

print("\n=======================================================\n")

# --> Removing unnecessary columns

# Removing unnecessary column is essential for data cleaning. You can delete single or multiple columns
# of DataFrame using DataFrame.drop() method.
print("Removings Column From a DataFrame")

df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6],"C":[7,8,9]}) # create a DataFrame
print("Original DataFrame:",df,sep='\n') # Desplay the Original DataFrame
df = df.drop(columns=["A","B"])   # Delete Columns A and B
print("DataFrame After Deleting Columns 'A' and 'B':")  # Display Update Data Frame
print(df)

print("\nRemovings Rows From a DataFrame\n")
# they have three types to removing Rows From DataFrame
# 1) Using drop() method (Similar to DataFrame.drop() method of a column)
print("Using 'drop()' method")

df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]}) # Create DataFrame
print("Original DataFrame:",df,sep='\n')  # Desplay the Original DataFarame
df = df.drop(1) # RemoveRow With Index 1
print("\n After Removing Row")
print(df)
'''
# 2) Removing Rows Based On Condition
print("\nRemoving Rows Based On Condition\n")

df = pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,10],"C":[11,12,13,0,15]},index = ["r1","r2","r3","r4","r5"])
print("Original Dataframe",df,sep='\n') # Desplaye Original DataFrame

result = df[df["C"]!= 0] # Dropping Rows Where Column 'C' contains 0

print("After dropping the row where 'C' has 0:")# Desplay The Result
print(result)
'''
# 3) Dropping Rows With Index Slicing
# This method is drop a range of rows based on their index positions.

print("\n Removing Rows Using Index Slicing: \n")

df = pd.DataFrame({"A":[1,2,3,4,5],"B":[6,7,8,9,10]}) # Create A DataFrame

print("Original DataFrame",df,sep='\n') #Desplay Original DataFrame

result = df.drop(df.index[2:4]) # Drop Tabel Using Indexing Slicing Method.

print("After Droping the row at 2 and 3:",result,sep="\n")
'''
