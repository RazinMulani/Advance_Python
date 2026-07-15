# Replace Empty Values:
# Replace NULL values with the number 120

import pandas as pd

df = pd.read_csv("scores.csv")

df.fillna(120,inplace = True)
print(df.to_string())
