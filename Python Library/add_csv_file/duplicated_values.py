# Removing Duplicates:
# Duplicates Rows are Rows that have been registered more than one time.


# Example:
# 
import pandas as pd

data = {"name":["Razin","Sami","Asjad","Razin","Sami"],
        "Age":[22,20,12,22,20]}
df = pd.DataFrame(data)
print(df)

print(df.duplicated())
