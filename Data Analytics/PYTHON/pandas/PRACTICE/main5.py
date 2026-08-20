# Level 5 — Challenge
# 19. Customer spending analysis 🔥🔥
# Calculate the total amount spent by each customer.
# Then find the top 5 customers based on total spending.

# Your result should contain:
# Customer
# Total_Sales

import pandas as pd
import numpy as np

data= pd.read_csv("D:/DATA_ANALYTICS/sales_data.csv")
df=pd.DataFrame(data)

colms=df.columns
print(colms)

#print(df[["Customer","Total_Sales"]])

cus_purchase=df.groupby("Customer")["Total_Sales"].sum()
cus_purchase=cus_purchase.sort_values(ascending=False).head(5)

print(cus_purchase.reset_index())

# #reset_index() ki zaroorat kyun?
# groupby() normally grouping wali column ko index bana deta hai.
# reset_index() bolta hai:
# "Is index ko wapas normal column bana do."

#without reset index => heere Customer ek index ki tara ahra hn or totalSales sirf colm show hora hn
# Customer
# Ahmed     125000
# Ali       110000
# Hamza      95000


# with reset index  => here Customer bhi ek colm bangaya hn total_salses k sat
#   Customer  Total_Sales
# 0 Ahmed        125000
# 1 Ali          110000
# 2 Hamza         95000
# 3 Sara          87000