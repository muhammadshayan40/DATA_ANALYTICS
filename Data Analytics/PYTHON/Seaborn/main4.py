import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

#seaborn also gives us sample data
data=sns.load_dataset('tips')
df=pd.DataFrame(data)
#print(df)

#Histrogram plot
sns.histplot(data=df, x="total_bill", kde=True, )
#kde se ek smooth curva ahta hn
#bins se hum ye define krty hn k kitny bars me data ko divide krna h

plt.title("Distribution of Total Bill")
plt.show()