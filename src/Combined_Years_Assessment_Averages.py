import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read in the combined data file
df = pd.read_csv('https://raw.githubusercontent.com/ds5110/project-jenrwen/main/acap_me/combined_assesments.csv?token=GHSAT0AAAAAABU2R74H5MMTQ3ISZXKDPXPUYXQKIFQ')

# averages of all assessments each year
def plot_combined_years(df):
  # get assessment outcomes list
  assessment_outcomes = df.columns[2:21].array
  # improvements between assessment 1 and 2 on average each year
  df_year = df.melt(id_vars=['Year', 'Assessment'], value_vars=assessment_outcomes, var_name='Outcomes', value_name='Assessment Score')
  # print(df_year.head(5))
  sns.set_theme(color_codes=True)
  # create plot
  sns.set(rc = {'figure.figsize':(15,10)})
  scores_plot = sns.barplot(x=df_year['Year'], y=df_year['Assessment Score'], hue=df_year['Assessment'])
  scores_plot.set_xlabel("School Year")
  scores_plot.set_title("2018-2021 Outcomes Averages")
 
plot_combined_years(df)
