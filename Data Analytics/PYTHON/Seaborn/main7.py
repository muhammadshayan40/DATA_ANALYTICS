#COUNT PLOT
#it is used to show the count of observations in each categorical bin using bars. It is similar to bar plot but it is used for categorical data.
#isme X ki vaalue deni hoti hn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips')
# print(data)

sns.countplot(data=data, x='day', hue='sex')
plt.show()