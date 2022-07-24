# Sanitize the ACAP-ME Childplus Outcomes Assessments
import pandas as pd

filename = "../data/ChildPlus Outcomes Assessments.csv"

# The encoding option allows for non-standard characters (probably of Windows origin)
df = pd.read_csv(filename, encoding = 'unicode_escape')

# This function replaces a name in the first column with with the integer from column 3
def clean(row):
  if isinstance(row[0], str) and "s Family" in row[0]:
    print(type(row[0]), row[0], row[2])
    row[0] = f"{row[2]:}'s Family"
    print(type(row[0]), row[0], row[2])

# Clean the dataframe
df.apply(clean, axis=1)

# Write the cleaned data to a CSV file
df.to_csv("ChildPlus_clean.csv", index=False)
