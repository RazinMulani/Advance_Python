# Replace Only One Specified Columns

import pandas as pd

df = pd.read_csv("scores.csv")
df.fillna({"First Score":130},inplace = True)
print(df.to_string())
