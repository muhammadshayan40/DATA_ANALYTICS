import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

#seaborn also gives us sample data
data=sns.load_dataset('tips')
df=pd.DataFrame(data)
#print(df)

#line plot
sns.lineplot(data=df, x="day", y="total_bill")

plt.title("Average Total Bill by Day")
plt.show()


