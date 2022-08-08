import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read in the combined data file
df = pd.read_csv('../acap_me/combined_asssessments.csv')

def organize_age_groups(df):
  # organize df by age group based on information from stakeholder
  df_class_groups = df.copy()
  df_class_groups.loc[:, 'Housing':'TOTAL'] = df_class_groups.loc[:, 'Housing':'TOTAL'].diff()
  df_class_groups = df_class_groups.loc[(df_class_groups['Assessment'] == 2)]
  
  # EHS and IT under age 3
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("EHS", na=False), 'Early Head Start (EHS)', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Early Head Start", na=False), 'Early Head Start (EHS)', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("I/T", na=False), 'Infant Toddler (IT)', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Infant/Toddler", na=False), 'Infant Toddler (IT)', inplace=True)
  
  # Head Start (HS), Preschool (PS), Early Intervention (could be Foundation or EI) ages 3-5, some 6
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains(" HS", na=False), 'Head Start (HS)', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Head Start", na=False), 'Head Start (HS)', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains(" PS", na=False), 'Preschool (PS)', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Preschool", na=False), 'Preschool (PS)', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Foundation", na=False), 'Early Intervention', inplace=True)

  return df_class_groups

def create_family_count_subplot(family_counts):
  # plot number of families in each category
  fig2, axes2 = plt.subplots(1, 4, figsize=(20, 10))
  fig2.tight_layout()
  fig2.suptitle('Number of Families Enrolled by Classroom Type', fontsize = 25, y=1.02)
  # loop through all four years
  i = 0
  for value in family_counts:
    count_plot = sns.barplot(x = value.index, y = value.values, ax=axes2[i],
                             order=['Early Head Start (EHS)', 'Infant Toddler (IT)', 'Head Start (HS)', 'Preschool (PS)', 'Early Intervention'])
    count_plot.set_xlabel("{}".format(2018+i), fontsize = 15)
    if i == 0:
      count_plot.set_ylabel("Number of Families Enrolled", fontsize = 20)
    sns.set_style("darkgrid")
    count_plot.tick_params(axis='x', rotation=90, labelsize = 15)
    count_plot.tick_params(axis='y', labelsize = 15)
    count_plot.axes.set_ylim(0, 120)
    i += 1
    
  plt.show()
    
def plot_families_classroom_type(df):
  # call function to organize age groups
  organize_age_groups(df)

  # get list of family counts by year
  family_count_2018 = df_class_groups.loc[(df['Year'] == '2018-2019')]['Classroom'].value_counts()
  family_count_2019 = df_class_groups.loc[(df['Year'] == '2019-2020')]['Classroom'].value_counts()
  family_count_2020 = df_class_groups.loc[(df['Year'] == '2020-2021')]['Classroom'].value_counts()
  family_count_2021 = df_class_groups.loc[(df['Year'] == '2021-2022')]['Classroom'].value_counts()
  family_counts = [family_count_2018, family_count_2019, family_count_2020, family_count_2021]
  
  # call function to create subplots
  create_family_count_subplot(family_counts)
  
plot_families_classroom_type(df)
