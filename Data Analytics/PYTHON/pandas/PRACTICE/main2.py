#LEVEL 2
import pandas as pd

data= pd.read_csv("D:/COMEB@CK/sales_data.csv")
df=pd.DataFrame(data)

#6)Display all orders where:City = Karachi
kar_orders=df[df['City']=='Karachi']
# print(kar_orders)

#_______________________________________________________
#7) Find all orders where:Total_Sales > 100000

expensive_ord=df[df['Total_Sales']>100000]
tot_exp_ord=(df['Total_Sales']>100000)
print(tot_exp_ord.sum())
# print(expensive_ord)

#___________________________________________________________
#8)Find orders where:City = Karachi AND Total_Sales > 100000

filter=df[(df['City']=="Karachi") & (df['Total_Sales']>100000)]
total_fil_VALUES=((df['City']=="Karachi") & (df['Total_Sales']>100000))
print(total_fil_VALUES.sum())
# print(filter)

#_________________________________________________________
#9)find orders wheere Product = Laptop OR Product = Phone
phone_LAP=df[((df['Product']=="Laptop") | (df['Product']=="Phone"))]
tot_ph_LP=((df['Product']=="Laptop") | (df['Product']=="Phone"))
print(tot_ph_LP.sum())
# print(phone_LAP)

#__________________________________________________________
#10)Sort the dataset by Total_Sales from highest → lowest.Then display the top 10 orders.

print(df.sort_values('Total_Sales', ascending=False).head(10))