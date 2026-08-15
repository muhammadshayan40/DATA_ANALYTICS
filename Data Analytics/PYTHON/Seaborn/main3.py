import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

#seaborn also gives us sample data
data=sns.load_dataset('tips')
df=pd.DataFrame(data)
print(df)

#Bar plot
sns.barplot(data=df, x="day", y="total_bill",hue='sex', order=["Sun","Sat","Fri","Thur"  ])

plt.title("Average Total Bill")
plt.show()