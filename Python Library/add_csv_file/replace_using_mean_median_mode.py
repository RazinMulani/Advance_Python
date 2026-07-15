# Replace Using Mean, Median, or Mode
# Calculate the MEAN, and replace any empty values with it:

import pandas as pd

def mean_m():
    df = pd.read_csv("scores.csv")
    x = df["First Score"].mean()
    df.fillna({"First Score":x},inplace = True)
    print(df.to_string())

mean_m()

def median_m():
    df = pd.read_csv("scores.csv")
    x = df["Second Score"].median()
    df.fillna({"Second Score":x},inplace = True)
    print(df.to_string())

median_m()

def mode_m():
    df = pd.read_csv("scores.csv")
    x = df["Forth Score"].mode()
    df.fillna({"Forth Score":x},inplace = True)
    print(df.to_string())

mode_m()
