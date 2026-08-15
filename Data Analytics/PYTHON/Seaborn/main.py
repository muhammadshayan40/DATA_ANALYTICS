#LINE PLOT
#Seaborn is easy,and advance V of matplotlib

import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

chota_data={
    'Days':['Mon','Tues','Wed','Thu','Fri','Sat','Sun'],
    'Age':[20,41,52,33,24,15,66],
}

df_chota=pd.DataFrame(chota_data)
print(df_chota)

#for color 
color_Pal=sns.color_palette('pastel')

sns.lineplot(data = df_chota, x='Age', y='Days',palette=color_Pal)
plt.show()

#here, in sns, sns.lineplot(data = df_chota, x='Age', y='Days',)
#yaha or bhi function de skte hn eg
# #hue='koi bhi colm do'=> hue will give us different color for different values of that colm
# style='koi bhi colm do'=> style will give us different line style for different values of that colm

#_____________________________________________________________

#seaborn also gives us sample data
data=sns.load_dataset('tips')
df=pd.DataFrame(data)
#print(df)


