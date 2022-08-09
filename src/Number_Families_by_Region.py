import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read in the combined data file
df = pd.read_csv('acap_me/combined_assessments.csv')

def organize_region_groups(df):
  # organize df by age group based on information from stakeholder
  df.loc[:, 'Housing':'TOTAL'] = df.loc[:, 'Housing':'TOTAL'].diff()
  df_class_groups = df.loc[(df['Assessment'] == 2)]
  
  # Classrooms by Region
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Caribou", na=False), 'Caribou', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Home Base", na=False), 'Home Base', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Gouldville", na=False), 'Gouldville', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Houlton", na=False), 'Houlton', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Dyer Brook", na=False), 'Houlton', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Region II", na=False), 'Houlton', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains(" PIRCTC", na=False), 'Goudville', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Birch", na=False), 'Birch', inplace=True)
  df_class_groups['Classroom'].mask(df['Classroom'].str.contains("Fort Kent", na=False), 'Fort Kent', inplace=True)
  
  return df_class_groups

def create_family_count_subplot(family_counts):
  # plot number of families in each category
  fig2, axes2 = plt.subplots(1, 4, figsize=(20, 10))
  fig2.tight_layout()
  fig2.suptitle('Number of Families Enrolled by Region', fontsize = 25, y=1.02)
  # loop through all four years
  i = 0
  for value in family_counts:
    count_plot = sns.barplot(x = value.index, y = value.values, ax=axes2[i],
                             order = ['Birch', 'Caribou', 'Goudville', 'Houlton', 'Fort Kent', 'Home Base',])
    count_plot.set_xlabel("{}".format(2018+i), fontsize = 15)
    if i == 0:
      count_plot.set_ylabel("Number of Families Enrolled", fontsize = 20)
    sns.set_style("darkgrid")
    count_plot.tick_params(axis='x', rotation=90, labelsize = 15)
    count_plot.tick_params(axis='y', labelsize = 15)
    count_plot.axes.set_ylim(0, 60)
    i += 1

  plt.show()

def plot_families_classroom_region(df):
  # call function to organize by region
  df_class_groups = organize_region_groups(df)

  # get list of family counts by year
  family_count_2018 = df_class_groups.loc[(df['Year'] == '2018-2019')]['Classroom'].value_counts()
  family_count_2019 = df_class_groups.loc[(df['Year'] == '2019-2020')]['Classroom'].value_counts()
  family_count_2020 = df_class_groups.loc[(df['Year'] == '2020-2021')]['Classroom'].value_counts()
  family_count_2021 = df_class_groups.loc[(df['Year'] == '2021-2022')]['Classroom'].value_counts()
  family_counts = [family_count_2018, family_count_2019, family_count_2020, family_count_2021]
  
  # call function to create subplots
  create_family_count_subplot(family_counts)

plot_families_classroom_region(df)
