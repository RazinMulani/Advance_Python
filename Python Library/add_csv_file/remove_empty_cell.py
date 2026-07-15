# One way to deal with empty cell is to remove rows that contain empty cell

import pandas as pd

df = pd.read_csv("scores.csv")
new_df = df.dropna()
print(new_df.to_string())

#(Note: By default, the dropna() method returns a new DataFrame, and will not change the original)
