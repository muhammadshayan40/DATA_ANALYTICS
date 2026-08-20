#Save & load data from CSV file
import pandas as pd

data={
    'Name' : ["Shayan", "Ali", "Sara" ,"Maryam"],
    'Age':[19,20,20,18],
    'Salary':[55000, 40000, 45000, 60000]
}

emp_data=pd.DataFrame(data)

csv=emp_data.to_csv('emp_data.csv', index=False) #index false krne se index column csv file me nahi aayega

#for load
load_data=pd.read_csv('emp_data.csv')
print(load_data)