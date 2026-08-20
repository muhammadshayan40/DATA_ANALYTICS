#LEVEL 4
import pandas as pd
import numpy as np

data= pd.read_csv("D:/COMEB@CK/sales_data.csv")
df=pd.DataFrame(data)

# 15. Sales by city,Calculate total sales for every city.
# Expected concept:groupby(),sum()

# Example output:
# Karachi       XXXXX
# Lahore        XXXXX
# Islamabad     XXXXX
# ==================================================================================
#GROUP BY CONCEPT CLEAR
# Manually Karachi ki rows alag karo, phir add karo; Lahore ki rows alag karo, phir add karo.

# Pandas mein:df.groupby("City")["Sales"].sum(), #phele jis ki uniques values chiye ho wo liko (eg CITY),then
                                               #then uski price add krni hn yah pir quantiy us colm ka name(eg Sales)

# Result:
# Karachi    200000
# Lahore     130000
#=================================================================
group_by=df.groupby("City")["Total_Sales"].sum()
print(group_by)

#________________________________________________________________
# 16. Average sales by product
# Find the average Total_Sales for each product.Then sort the result from highest to lowest.


print(df['Product'].unique())

avg_sales=df.groupby("Product")["Total_Sales"].mean()
avg_sales=avg_sales.sort_values(ascending=False)
print(avg_sales)

#sum() → total sales
#mean() → average sales
#_______________________________________________________
#17. Quantity sold by product
# Find the total quantity sold for each product.
# Then answer:Which product was sold in the highest quantity?

# print(df['Product'].unique())
total_sold=df.groupby("Product")["Quantity"].sum()
total_sold=total_sold.sort_values(ascending=False)
print(total_sold)

item_quantity=total_sold.max()
name=total_sold.idxmax() #for name use idx max

print(f"Highest quantity product: {name}" )
print(f"Quantity sold: {item_quantity}" )

#_________________________________________________________
#18. Department analysis 🔥
# For each department, calculate:
# Total sales
# Average sales
# Total quantity

total_sales=df.groupby("Department")["Total_Sales"].sum()
avg_sales=df.groupby("Department")["Total_Sales"].mean()
total_quantity=df.groupby("Department")["Quantity"].sum()

print("Total Sales of DEPARTMENT:")
print(total_sales)

print("Total Sales of DEPARTMENT:")
print(avg_sales)

print("Total Quantities of DEPARTMENT:")
print(total_quantity)

#BUT THERE IS BETTER APPROCH 
#use agg

# df.groupby("GROUP_COLUMN").agg(
#     New_Name=("Column", "function"),
#     New_Name=("Column", "function")
# )

depart_analysis=df.groupby("Department").agg(
    Total_Sales=("Total_Sales", "sum"),
    Average_Sales=("Total_Sales", "mean"),
    Total_Quantity=("Quantity", "sum")
    
)

print(depart_analysis)