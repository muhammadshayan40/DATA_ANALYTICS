#PAIR PLOT
#it is used to show the pairwise relationship between the features in the dataset. It is

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips')
# print(data)

sns.pairplot(data=data, hue='sex')
plt.show()

#ye practice k times smj lena