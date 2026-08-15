import matplotlib.pyplot as plt
import pandas as pd

#how to show data in bar graph using pandas
df = pd.read_csv("D:/COMEB@CK/employees_dataset.csv")
print(df)

plt.bar(df["Name"], df["Department"])
plt.xlabel("Name")
plt.ylabel("Department")
plt.show()

#how to save any chart 
plt.savefig("D:/COMEB@CK/bar_chart.png") #give the location where you want to save the chart and give the name of the chart with extension
plt.savefig("bar.png")
