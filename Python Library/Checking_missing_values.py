# Pandas
# Preprocessing On DataBase: Null Values, Duplicates Values
'''
# 1. Checking for Missing Values Using "isnull()" and "notnull()"

import pandas as pd

import numpy as np

dict = {"First Score":[100,90,np.nan,95],
        "Second Score":[30,45,56,np.nan],
        "Third Score":[np.nan,40,80,98]}
df = pd.DataFrame(dict)
print(df)
# Using "isnull()" method
print("===============Using 'isnull()' method=================")

# if value is number show the False
# and if values is not a number(NaN) show the

print(df.isnull())

# Using "notnull()" method
print("===============Using 'notnull()'

# if value is number show the True
# and if values is not a number(NaN) show the

print(df.notnull())
'''
# 2. Filling Missing Values Using fillna(), replace(), and interpolate()
#   Method              Desription
# 1. fillna()       Fill Missing Values with a constant and statistics
# 2. replace()      Replace Specific Values Including NaN
# 3. interpolate()  Estimate Missing Values Based On Surrounding Data
'''
import pandas as pd
import numpy as np

data = {
    "First Score":[100,90,np.nan,95],
    "Second Score":[30,np.nan,45,56],
    "Third Score":[np.nan,40,80,98],
    "Forth Score":[np.nan,np.nan,np.nan,65]
    }
df = pd.DataFrame(data)
print("Original Data Frame:\n",df)

# 1. Fill Missing Values Using fillna()
df_fillna = df.fillna(df.mean())
print(f"\nAfter filna()(Using Column Mean):\n",df_fillna)

# 2. Replace Missing values using replace()
df_replace = df.replace(np.nan,0)
print("After replace() (NaN Replaced With '0'):\n",df_replace)

# 3. Fill Missing Values Using interpolate()
df_interpolate = df.interpolate()
print("After interpolate():\n",df_interpolate)
'''
# 3. Dropping Missing Values Using dropna():
# Remove the all missing values (NaN) rows from data frame and series

import pandas as pd
import numpy as np

data = {
    "First Score":[100,90,np.nan,95],
    "Second Score":[30,np.nan,45,56],
    "Third Score":[np.nan,40,80,98],
    "Forth Score":[np.nan,np.nan,np.nan,65]    
    }

df = pd.DataFrame(data)
print("Before Using dropna():\n",df)
# Drop rows with any missing values

df_dropna = df.dropna()
print("After Using dropna():\n",df_dropna)





