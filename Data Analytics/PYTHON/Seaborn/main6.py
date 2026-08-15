#HEat MAP
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips')
print(data)

gp = data.groupby("day").agg({"tip": "mean"})
sns.heatmap(gp)
plt.show()