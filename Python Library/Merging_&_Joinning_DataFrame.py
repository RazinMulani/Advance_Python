# Merging And Joinning DataFrames:

# When Working With multiple DataFrames, we often need to combine them into a single DataFrame.
# pandas Provide Three Main Methods:

# 1) Merge: Combine data frame using Common Columns(like To SQL JOIN)
# Ther Are Four Basic Ways To Handles The Join (Inner, Left, Right and Outer)
# Syntax: DataFrame.merge(right,on,left_on,right_on,left_index,right_index,sort,suffixes,copy,indicator,
#                        validate)
print("1. Merging Methods")
#Example:
import pandas as pd
import numpy as np

data1 = {'key':['K0','K1','K2','K3'],
         'Name':['Razin','Sami','Asjad','Shabnoor'],
         'Age':[22,20,12,24]}

data2 = {'key':['K0','K1','K2','K3'],
         'Address':['Pune','Mumbai','Surat','Delhi'],
         'Qualification':['B.tech','BSC','BE','B.Com']}

df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2)

print(df,'\n\n',df1)
# Merging DataFrame Using One Key
print("Merge Table:")
res = pd.merge(df,df1,on='key')
print(res)

print('\n=====================================================\n')

# Parametrs of Merge():
print("Parametrs OF Merge:")
# 1) left : The First (left) DataFrame To Merge
print("Left = df")
print('\n=====================================================\n')

# 2) right : The secand (right) DataFrame to Merge
print("Right = df1")

print('\n=====================================================\n')

# 3) How : how='left','right','outer','inner','cross': optional. Default 'inner'.Specific how to merge
print("how parameters")
print("1. Inner")
res_inner= pd.merge(df,df1,on="key",how="inner")
print(res_inner)
print("\n------------------------------------------------------\n")
print("2. Left")
res_left = pd.merge(df,df1,on="key",how="left")
print(res_left)
print("\n------------------------------------------------------\n")
print("3. Right")
res_right = pd.merge(df,df1,on="key",how="right")
print(res_right)
print("\n------------------------------------------------------\n")
print("4. Outer")
res_outer = pd.merge(df,df1,on="key",how="outer")
print(res_outer)
print("\n------------------------------------------------------\n")
print("5. Cross")
res_cross = pd.merge(df,df1,how="cross")
print(res_cross)

print('\n=====================================================\n')
# 4) On : valuse: String, List: Optional. Specific in what level to do the merging
print("4. On Parameter")
res_on = pd.merge(df,df1,on="key")
print(res_on)

# 5) left_on : Optional. Specifies in what level to do the merging on the DataFrame to the left

print("5. left_on Parameter")
res_left_on = pd.merge(df,df1,left_on="key",right_on="key")
print(res_left_on)


print('\n=====================================================\n')
# 2) Join: Join DataFrameUsing There Index(Or A Key Valume)
# I) Joining DataFrames Using .join()
data1 = {'Name':['Jai','Princi','Gaurav','Anuj'],
         'Age':[27,24,22,32]}
data2 = {'Address':['Pune','Mumbai','Pune','Mumbai'],
         'Qualification':['MCA','Phd','Bcom','B.hons']}

df = pd.DataFrame(data1,index=['k0','k1','k2','k3'])

df1 = pd.DataFrame(data2,index=['k0','k1','k2','k3'])
print("Orignal DataFrame\n",df,'\n\n',df1)

# Use .join() method
print("\n******************************************************\n")
print("Joining A Table\n",df.join(df1))

print("\n******************************************************\n")
# Use how = 'outer' in order to get union
print("If your index have Extra value Here, outer keeps all indexes from both DataFrames, filling missing values with NaN.")
data3 = {'Name':['Jai','Princi','Gaurav','Anuj'],
         'Age':[27,24,22,32]}
data4 = {'Address':['Pune','Mumbai','Pune','Mumbai'],
         'Qualification':['MCA','Phd','Bcom','B.hons']}

df2 = pd.DataFrame(data3,index=['k0','k1','k2','k3'])

df3 = pd.DataFrame(data4,index=['k1','k1','k2','k3']) # if your index have extra value
print("Orignal DataFrame\n",df2,'\n\n',df3)

res1 = df2.join(df3,how='outer')
print(res1)
print("\n******************************************************\n")

# 2. Joining DataFrame Using The "on" Argument
# If you want to join DataFrame based on columns (rather than the index), we can use "on" argument.

data5 = {'Key':['k0','k1','k2','k3'],
         'Name':['Jai','Princi','Gaurav','Anuj'],
         'Age':[27,24,22,32]}
data6 = {'Key':['k0','k1','k2','k3'],
         'Address':['Pune','Mumbai','Pune','Mumbai'],
         'Qualification':['MCA','Phd','Bcom','B.hons']}

df4 = pd.DataFrame(data5)

df5 = pd.DataFrame(data6)
df5 = df5.set_index('Key') # Importan Line of Code 
print("Orignal DataFrame\n",df4,'\n\n',df5)

print("Using On\n")
res2 = df4.join(df5,on='Key')
print(res2)
print("\n******************************************************\n")

# 3. Joining DataFrame With Different Index Levels(Multi-Index)
print("Joining DataFrame With Different Index Levels(Multi-Index)")

data7 = {'Name':['Jai','Princi','Gaurav'],
         'Age':[27,24,22]}
data8 = {'Address':['Pune','Mumbai','Pune','Mumbai'],
         'Qualification':['MCA','Phd','Bcom','B.hons']}

df6 = pd.DataFrame(data7,index = pd.Index(['k0','k1','k2'],name='Key'))
index = pd.MultiIndex.from_tuples([('k0','y0'),('k1','y1'),('k2','y2'),('k2','y3')],names=['Key','y'])
df7 = pd.DataFrame(data8,index=index)

print(df6,'\n\n',df7)                                                                                         
print("\n******************************************************\n")
# use how="inner": join single index data frame with multt-index DataFrame

result = df6.join(df7,how='inner')
print(result)
# 3) Concat: Stacks DataFrames either vertically or horizontally.
