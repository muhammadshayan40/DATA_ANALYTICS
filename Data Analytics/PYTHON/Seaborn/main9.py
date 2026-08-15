#BOXPLOT
#it is used to show the distribution of a continuous variable across different categories. It is

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips')
# print(data)

sns.boxplot(data=data, x='sex',y='tip',orientation='vertical')
plt.show()