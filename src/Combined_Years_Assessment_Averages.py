import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read in the combined data file
df = pd.read_csv('acap_me/combined_assessments.csv')

# averages of all assessments each year
def plot_combined_years(df):
  # get assessment outcomes list
  assessment_outcomes = df.columns[2:21].array
  # improvements between assessment 1 and 2 on average each year
  df_year = df.melt(id_vars=['Year', 'Assessment'], value_vars=assessment_outcomes, var_name='Outcomes', value_name='Assessment Score')
  # print(df_year.head(5))
  sns.set_theme(color_codes=True)
  # create plot
  sns.set_style("darkgrid")
  sns.set(rc = {'figure.figsize':(15,10)})
  scores_plot = sns.barplot(x=df_year['Year'], y=df_year['Assessment Score'], hue=df_year['Assessment'])
  scores_plot.set_xlabel("School Year")
  scores_plot.set_title("2018-2021 Outcomes Averages")
  plt.show()
 
plot_combined_years(df)
