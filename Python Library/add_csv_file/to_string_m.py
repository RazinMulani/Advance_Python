#Note to_string() to print intire data frame

import pandas as pd
import numpy as np

df = pd.read_csv("scores.csv")
print(df.to_string())
