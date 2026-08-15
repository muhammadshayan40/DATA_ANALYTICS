import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv("D:/COMEB@CK/restaurant_sales_data.csv")

df=pd.DataFrame(data)
print(df)

plt.scatter(df["Quantity"], df["Total_Sales"])

plt.title("Quantity vs Total Sales")
plt.xlabel("Quantity Sold")
plt.ylabel("Total Sales (PKR)")
plt.grid(True)

plt.show()