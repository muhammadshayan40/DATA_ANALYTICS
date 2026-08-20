import pandas as pd 

#creating a dataframe
df=pd.DataFrame([1,2,3], columns=['Col_name'])
print(df)

#understaning dataframe and its func/methods

data={
    'Name' : ["Shayan", "Ali", "Sara" ,"Maryam"],
    'Age':[19,20,20,18],
    'Salary':[55000, 40000, 45000, 60000]
}

emp_data=pd.DataFrame(data)
print(emp_data)