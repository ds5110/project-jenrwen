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

def create_class_changes_subplot(class_changes):
  # call function to organize age groups
  assessment_outcomes = df.columns[2:21].array

  # plot class changes every year
  fig2, axes2 = plt.subplots(1, 4, figsize=(20, 10))
  fig2.tight_layout()
  fig2.suptitle('Average Change in Assessment Score by Region', fontsize = 25, y=1.02)
  # loop through all four years
  i = 0
  for value in class_changes:
    value = value.melt(id_vars=['Year', 'Assessment', 'Classroom'], value_vars=assessment_outcomes, var_name='Outcomes', value_name='Assessment Score')
    scores_plot = sns.barplot(x = value['Classroom'], y = value['Assessment Score'], ax=axes2[i],
                             order = ['Birch', 'Caribou', 'Goudville', 'Houlton', 'Fort Kent', 'Home Base',])
    scores_plot.set_xlabel("{}".format(2018+i), fontsize = 15)
    if i == 0:
      scores_plot.set_ylabel("Average Change in Assessment Score", fontsize = 20)
    else:
      scores_plot.set(ylabel=None)
    sns.set_style("darkgrid")
    scores_plot.tick_params(axis='x', rotation=90, labelsize = 15)
    scores_plot.tick_params(axis='y', labelsize = 15)
    scores_plot.axes.set_ylim(-0.5, 0.75)
    scores_plot.axhline(0, color = 'black')
    i += 1
  plt.show()

def plot_change_classroom_type(df):
  # call function to organize by region
  df_class_groups = organize_region_groups(df)

  # get list of average changes by year
  df_classes_2018 = df_class_groups.loc[(df['Year'] == '2018-2019')]
  df_classes_2019 = df_class_groups.loc[(df['Year'] == '2019-2020')]
  df_classes_2020 = df_class_groups.loc[(df['Year'] == '2020-2021')]
  df_classes_2021 = df_class_groups.loc[(df['Year'] == '2021-2022')]
  class_changes = [df_classes_2018, df_classes_2019, df_classes_2020, df_classes_2021]
  
  # call function to create subplots
  create_class_changes_subplot(class_changes)

plot_change_classroom_type(df_copy)
