import pandas as pd
import numpy as np

filename = "Family_outcomes_2021-2022.csv"

# The encoding option allows for non-standard characters (probably of Windows origin)
df = pd.read_csv(filename, encoding = 'unicode_escape')

col = dict(zip(df.columns,df.iloc[3]))
#col = df.loc[3].to_numpy()
print(col)
#new_df.columns = columns
#new_df = pd.DataFrame(columns=col)
df.rename(columns=col, inplace=True)
#df.rename(index={1: "Classroom"})
print(df.head(3))

df.drop([0,1,2,3], axis=0, inplace=True)

# drop the empty columns
df.dropna(how='all', axis=1, inplace=True)

#df.drop([1,2,3], axis=0, inplace=True)

#remove calculated data
#df = df[~df["Family"].str.contains("ACAP", na=False)]
df = df[~df["Assessment"].str.contains("-", na=False)]

df["Classroom"] = None
df.ffill(axis=1, inplace=True)
df.ffill(axis=0, limit=1, inplace=True)

df = df[~df["Family"].str.contains('Average|complete|Scoring|Gains', regex=True)]

#df.Classroom = df.Classroom.replace(to_replace="^[0-9]{2}$", value=None)
df.Classroom = df.Classroom[~df.Classroom.str.contains('^[0-9]{2}$', regex=True)]
df.ffill(axis=0, inplace=True)
df = df[~df["Family"].str.contains("ACAP", na=False)]

#filter = isinstance(df["Classroom"], str)
#df["Classroom"].where(filter,inplace=True)

#for column in df[["Classroom"]]:
#    for value in df[column].values:
#        if isinstance(value, int):
#            value = None
#    print(df[column])

#df.loc[isinstance(df["Classroom"], int), "Classroom"] = None

#df["Classroom"] = df["Classroom"].replace(88,None)

df.drop_duplicates(inplace=True)
df["Year"] = "2021-2022"

# This function replaces a name in the first column with with the integer from column 3
#def clean(row):
    #print(type(row))
    #if isinstance(row[0], str) and "ACAP" in row[0]:
    #    print(type(row[0]), row[0], row[2])
    #    df.drop(row[0], axis=0)
    #if isinstance(row[3], str) and "1" in row[3]:
        #print(row)
        #new_df = pd.concat([new_df, row])

# Clean the dataframe
#df.apply(clean, axis=1)
#print(new_df)
#df[df[0].str.contains("ACAP")==False]

# Write the cleaned data to a CSV file
df.to_csv("2021-2022_assessment_organized.csv", index=False)

print("organized")
