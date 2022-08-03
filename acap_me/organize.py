import pandas as pd
import numpy as np

#read all the files
filename2018 = "Family_outcomes_2018-2019.csv"
filename2019 = "Family_outcomes_2019-2020.csv"
filename2020 = "Family_outcomes_2020-2021.csv"
filename2021 = "Family_outcomes_2021-2022.csv"

# The encoding option allows for non-standard characters (probably of Windows origin)
df2018 = pd.read_csv(filename2018, encoding = 'unicode_escape')
df2019 = pd.read_csv(filename2019, encoding = 'unicode_escape')
df2020 = pd.read_csv(filename2020, encoding = 'unicode_escape')
df2021 = pd.read_csv(filename2021, encoding = 'unicode_escape')

def clean(df, year):
    #get the names from the 4th row
    col = dict(zip(df.columns,df.iloc[3]))
    #col = df.loc[3].to_numpy()
    #print(col)
    #new_df.columns = columns
    #new_df = pd.DataFrame(columns=col)
    
    #rename the columns to the names of the 4th row
    df.rename(columns=col, inplace=True)
    #df.rename(index={1: "Classroom"})
    #print(df.head(3))

    #drop the first 4 rows because there is no useful info
    df.drop([0,1,2,3], axis=0, inplace=True)

    # drop the empty columns
    df.dropna(how='all', axis=1, inplace=True)

    #df.drop([1,2,3], axis=0, inplace=True)

    #remove calculated assesment data (+/- rows)
    #df = df[~df["Family"].str.contains("ACAP", na=False)]
    df = df[~df["Assessment"].str.contains("-", na=False)]

    #Make a new column for classroom
    df["Classroom"] = None
    #Forward fill the classroom names to the whole row
    df.ffill(axis=1, inplace=True)
    #forward fill the family names and IDs down 1
    df.ffill(axis=0, limit=1, inplace=True)

    #remove calcuated averages and scoring legend
    df = df[~df["Family"].str.contains('Average|complete|Scoring|Gains', regex=True)]

    #clear out the digits that were forward filled in the Classroom column
    #df.Classroom = df.Classroom.replace(to_replace="^[0-9]{2}$", value=None)
    df.Classroom = df.Classroom[~df.Classroom.str.contains('^[0-9]{2}$', regex=True)]
    #forward fill the classroom names to fill in the emptied digit slots
    df.ffill(axis=0, inplace=True)
    #remove the rows that were just forawrd filled classroom names
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

    #drop duplicates - do we maybe want to keep these?
    df.drop_duplicates(inplace=True)
    #add a year column and include the year of the file
    df["Year"] = year

    # This function replaces a name in the first column with with the integer from column 3
    #def clean(row):
        #print(type(row))
        #if isinstance(row[0], str) and "ACAP" in row[0]:
        #    print(type(row[0]), row[0], row[2])
        #    df.drop(row[0], axis=0)
        #if isinstance(row[3], str) and "1" in row[3]:
            #print(row)
            #new_df = pd.concat([new_df, row])

#clean the dataframes
clean(df2018, "2018-2019")
clean(df2019, "2019-2020")   
clean(df2020, "2020-2021")   
clean(df2021, "2021-2022")   
            
# Clean the dataframe
#df.apply(clean, axis=1)
#print(new_df)
#df[df[0].str.contains("ACAP")==False]

concat_df = pd.concat([df2018, df2019, df2020, df2021])

# Write the cleaned data to a CSV file
df.to_csv("test_organized.csv", index=False)
print("organized")
