# If you want to Change the original DataFrame, use the inplace = True argument:

#Example

# Remove all rows with NULL values

import pandas as pd

df = pd.read_csv("scores.csv")
df.dropna(inplace = True)

print(df.to_string())
