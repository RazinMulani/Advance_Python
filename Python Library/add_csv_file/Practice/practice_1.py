# Practice
'''
Read the CSV file.
Print the complete DataFrame using to_string().
Find duplicate rows.
Display only duplicate rows.
Remove duplicate rows.
Count the number of null values in each column.
Replace the null values in Math using the mean.
Replace the null values in Science with 80.
Replace the null values in English using the median.
Save the cleaned DataFrame as cleaned_scores.csv.
'''
import pandas as pd

# Read The CSV File
df = pd.read_csv("practice_scores.csv")
print(df)

# Print the complete DataFrame using to_string()

print(df.to_string())

# Find Duplicate rows
print(df.duplicated(subset = ["Name","Math","Science","English"]))

# Display only duplicates rows
duplicates = df[df.duplicated(subset = ["Name","Math","Science","English"])]
print(duplicates)

# Remove Duplicates Rows.
print(df.drop_duplicates(subset = ["Name","Math","Science","English"]))

# Count The Number Of Null Values In Each Column
print(df.isnull())

# Replace the Null Values In Math Using The Mean.
x = df["Math"].mean()
df.fillna({"Math":x},inplace = True)
print(df.to_string())

# Replace the null values in Science with 80.
df.fillna({"Science":80},inplace = True)
print(df.to_string())

# Replace the null values in English using the median.
y = df["English"].median()
df.fillna({"English":y},inplace = True)
print(df.to_string())

# Save the cleaned DataFrame as cleaned_scores.csv.
df.to_csv("cleaned_scores.csv", index = False)
print("File saved successfully as cleaned_scores.csv")
