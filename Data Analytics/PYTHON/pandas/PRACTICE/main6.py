#FINAL CHALLENGE 🚀

# Create a complete Sales Analysis using Pandas.

# Find:
# Total overall sales
# Average order value
# Best-selling product
# Highest-revenue product
# Best-performing city
# Department with highest sales
# Most common payment method
# Average customer rating
# Number of cancelled orders
# Top 5 customers by spending
# ------------------------------------------------
# Try to produce:
# ===== SALES ANALYSIS =====
 
# Total Sales:
# Average Order Value:
# Best Selling Product:
# Highest Revenue Product:
# Best City:
# Best Department:
# Most Common Payment Method:
# Average Rating:
# Cancelled Orders:
# Top Customer:

import pandas as pd
import numpy as np

data= pd.read_csv("D:/DATA_ANALYTICS/sales_data.csv")
df=pd.DataFrame(data)

colms=df.columns
#print(colms)

Overall_sales=df["Total_Sales"].sum()
avg_order=df["Total_Sales"].mean()
best_product=df.groupby("Product")["Quantity"].sum().idxmax()
highest_revenue=df.groupby("Product")["Total_Sales"].sum().idxmax()
best_city=df.groupby("City")["Total_Sales"].sum().idxmax()
best_Department=df.groupby("Department")["Total_Sales"].sum().idxmax()
Pay_method=df["Payment_Method"].value_counts().idxmax()
avg_rating=df["Rating"].mean()
cancel_orders=(df["Status"]=="Cancelled").sum()

#TOP % CUSTOMERS
top5_customers=df.groupby("Customer")["Total_Sales"].sum()
top5_customers=top5_customers.sort_values(ascending=False).head(5)

#______________________DEIGNING THE OUTPUT____________________

print("\n ========== SALES ANALYSIS ========= \n")

print("Total Sales:",Overall_sales)
print("Average Order Value:",avg_order)
print("Best Selling Product:",best_product)
print("Highest Revenue Product:",highest_revenue)
print("Best City:",best_city)
print("Best Department:",best_Department)
print("Most Common Payment Method:",Pay_method)
print("Average Rating:",avg_rating)
print(f"Cancelled Orders:{cancel_orders} \n" )

print("========= Our Top 5 Customers =========")
print(top5_customers)