import pandas as pd 

#understaning dataframe and its func/methods

#data ko alag se defined kr k use krlo ya csv ya excel file se file use krlo zada better hoga

data={
    'Name' : ["Shayan", "Ali", "Sara" ,"Maryam"],
    'Age':[19,20,20,18],
    'Salary':[55000, 40000, 45000, 60000]
}

emp_data=pd.DataFrame(data)
print(emp_data)



#dataframe functions
print(emp_data.head()) #give first top 5 rows
print(emp_data.tail()) #give last 5 rows
print(emp_data.shape) #give shape of dataframe
print(emp_data.info()) #give information about the dataframe
print(emp_data.describe()) #give statistical information about the dataframe
print(emp_data.columns) #give columns of the dataframe
print(emp_data.rename(columns={'Name': 'Employee Name'})) #rename columns of the dataframe

#Rename wala imp hn