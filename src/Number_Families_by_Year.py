import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# read in the combined data file
df = pd.read_csv('https://raw.githubusercontent.com/ds5110/project-jenrwen/main/acap_me/combined_assesments.csv?token=GHSAT0AAAAAABU2R74HMFYXLNQADKW4BVMWYXQMHLA')

# number of families enrolled each year
def plot_num_fam(df):
  family_count = df.loc[(df['Assessment'] == 1)]['Year'].value_counts()
  family_count_plot = sns.barplot(x = family_count.index, y = family_count.values, 
                                  order = ['2018-2019','2019-2020','2020-2021', '2021-2022'])
  sns.set(rc = {'figure.figsize':(15,10)})
  family_count_plot.set_xlabel("School Year", fontsize = 20)
  family_count_plot.set_ylabel("Number of Families Enrolled", fontsize = 20)
  family_count_plot.set_title("Number of Families Enrolled by Year", fontsize=20)
  
plot_num_fam(df)
