#LEVEL 3
import pandas as pd
import numpy as np

data= pd.read_csv("D:/COMEB@CK/sales_data.csv")
df=pd.DataFrame(data)


#11. Create a new column 
# Create:Revenue_Per_Item ,Formula:Total_Sales / Quantity
df['Revenue_Per_Item']=(df['Total_Sales'])/(df['Quantity'])
print(df[['Revenue_Per_Item','Total_Sales', 'Quantity']])

#_________________________________________________
# 12. Create an age group,Create a new column called:Age_Group

# Rules:
# Age < 25       → Young
# 25–40          → Adult
# Age > 40       → Senior

#===NEW THING TO LEARN===
#np.select(
#     [condition1, condition2, condition3],
#     [value1, value2, value3]
# )

df['Age_Group']=np.select(
    [df['Age']<25, df['Age'].between(25, 40), df['Age']>40 ],
    ["Young", "Adult", "Senior"],
    default="Unknown" #yaaha agr defalut nhi liko gy toh,AGR TUMHE OUTPUT ME STINGS chiye hn toh default ki value 0 set hn jis se error ahyga
)

print(df[['Age','Age_Group']].head(10))

#_____________________________________________________
#13. Find the most expensive products,Find the 5 orders with the highest Unit_Price.
# Display:

# Product
# Unit_Price
# Customer

top_5=(df.sort_values('Unit_Price', ascending=False).head(5))
print(top_5[["Product", "Unit_Price", "Customer"]])

#______________________________________________________
# 14. Find cancelled orders,Filter all orders where:Status = Cancelled
# Then calculate the total value of cancelled orders.

total_cancel=df[df['Status']=="Cancelled"]
sumOF_canORDERS=df['Status']=="Cancelled"
#print(total_cancel)
print(sumOF_canORDERS.sum())

#