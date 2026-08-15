#topic7 =>WORKING WITH DATE VALUES ,I M SKIPPING THIS TOPIC

#topic8 handling with missing values
import pandas as pd

data={
    'Name' : ["Shayan", "Ali", "Sara" ,"Maryam"],
    'Age':[19,20,20,18],
    'Salary':[55000, 40000, 45000, 60000]
}

emp_data=pd.DataFrame(data)

#lets make one missing value in our emp_data
emp_data.loc[emp_data['Name'] == 'Maryam', 'Age'] = None
print(emp_data)

#how to check our database me kaha kah null value
print(emp_data.isnull().sum())

#and to fill those null values we can use fillna method
emp_data.fillna(0, inplace=True)
print(emp_data)
