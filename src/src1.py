import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read the dataframe of a specific year
df = pd.read_csv('')

# returns list of means 
def get_mean_list(column_means):
  mean_list = []
  for mean in column_means[1:-1]:
    mean_list.append(mean)
  return mean_list

# returns list of means for each outcome of both assessments
def get_assessment_means(df):
  df_first_assessment = df.iloc[0::2]
  df_second_assessment = df.iloc[1::2]
  column_first_mean = df_first_assessment.mean(axis=0)
  column_second_mean = df_second_assessment.mean(axis=0)
  first_list = get_mean_list(column_first_mean)
  second_list = get_mean_list(column_second_mean)
  assessment_means = first_list + second_list
  return assessment_means

# returns dataframe of assessment means for given year
def create_means_df(assessment_means):
  df_means = pd.DataFrame({'Assessment Outcome': ['Housing', 'Health and Wellness',	'Food/Nutrition',
                                'Transportation', 'Employment', 'Financial Literacy',
                                'Family Safety', 'Heating', 'Family Relationships',
                                'Child Development/Parenting Skills', 'Family Literacy', 'School Readiness',
                                'Education/Training', 'Family Engagement', 'Childs Educational Transitions',
                                'Life Transitions', 'Family Relationships', 'Community Involvement', 'Leadership and Advocacy', 
                                'Housing', 'Health and Wellness',	'Food/Nutrition',
                                'Transportation', 'Employment', 'Financial Literacy',
                                'Family Safety', 'Heating', 'Family Relationships',
                                'Child Development/Parenting Skills', 'Family Literacy', 'School Readiness',
                                'Education/Training', 'Family Engagement', 'Childs Educational Transitions',
                                'Life Transitions', 'Family Relationships', 'Community Involvement', 'Leadership and Advocacy'],
                        'Score': assessment_means,
                   'Assessment': ['A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1',
                                  'A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1', 
                                  'A1', 'A1', 'A1', 'A2', 'A2', 'A2', 'A2', 
                                  'A2', 'A2', 'A2', 'A2', 'A2', 'A2', 'A2', 'A2',
                                  'A2', 'A2', 'A2', 'A2', 'A2', 'A2', 'A2']})
  return df_means

# plots the mean values between assessments for each outcome
def plot_year_means(df, year):
  assessment_means = get_assessment_means(df)
  df_means = create_means_df(assessment_means)
  sns.set(rc = {'figure.figsize':(20,10)})
  ax = sns.barplot(x='Assessment Outcome', y='Score', hue='Assessment', data=df_mean)
  ax.set(title='{} Average Assessment Scores'.format(year))
  ax.set(xlabel='Assessment Outcomes', ylabel='Average Assessment Scores')
  ax.tick_params(axis='x', rotation=90)
  
plot_year_means(df)
