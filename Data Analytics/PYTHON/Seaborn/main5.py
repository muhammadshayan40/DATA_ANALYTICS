import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

#seaborn also gives us sample data
data=sns.load_dataset('tips')
df=pd.DataFrame(data)
#print(df)

#Scatter plot
sns.scatterplot(data=df,x="total_bill",y="tip", hue="sex")

plt.title("Total Bill vs Tip")
plt.show()