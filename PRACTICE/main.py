import pandas as pd

data= pd.read_csv("D:/COMEB@CK/sales_data.csv")
df=pd.DataFrame(data)

print(df.head(10))
#___________________________________________________________________
#2)Understand the dataset Find:Number of rows & colms, colm names, data types
print(df.columns)
print(df.info())

#___________________________________________________________________
#3)Display only:Customer, City, Product, Total_Sales
print(df[['Customer', 'City', 'Product', 'Total_Sales']])

#___________________________________________________________________
#4)Find all unique:Customer, City, Product, Total_Sales
#unique se ek colm me kitni different value hn ye pata chaltea hn

# Unique Cities
print(df['City'].unique())

# Unique Products
print(df['Product'].unique())

# Unique Departments
print(df['Department'].unique())

# Unique Payment Methods
print(df['Payment_Method'].unique())

# Number of Unique Cities
print(df['City'].nunique())

#___________________________________________________________________
#Q5)Try:df.describe(),,Then find the average/mean age and average/mean rating.
print(df.describe())

print(df['Age'].mean())
print(df['Rating'].mean())
#________________________________________________________________
