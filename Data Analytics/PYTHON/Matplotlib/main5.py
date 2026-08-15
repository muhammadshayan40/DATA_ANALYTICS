#PIE CHART
import matplotlib.pyplot as plt

brands=['Apple', 'Samsung', 'Huawei', 'Oppo', 'Vivo']
x=[30,56,12,8,2]
explode=[0,0,0,0.1,0] # this func cut the slice fom the pie chart
colors=['red','blue','green','yellow','orange']

plt.pie(x, labels=brands, explode=explode, colors=colors, autopct='%1.1f%%')
#autopct is used to show the percentage of each slice in the pie chart

plt.show()