#ROWS & COLM SELECTIONS
import pandas as pd

data={
    'Name' : ["Shayan", "Ali", "Sara" ,"Maryam"],
    'Age':[19,20,20,18],
    'Salary':[55000, 40000, 45000, 60000]
}

emp_data=pd.DataFrame(data)

#for colm

# print(emp_data[['Name']])
# print(emp_data[['Name','Salary']]) # for multiples colms & double bracket lagane se dataframe me aaega single bracket lagane se series me aaega

#-----------------------------------------------------
#FOR ROWS, there r 2 methods,
#1. loc[] =>isme row ki likte hn or filter krte hn
#2. iloc[] => isme idex dete hn or slicing ki tara bhi use krte hn

#method one
# print(emp_data.loc[emp_data.Name=='Maryam'])
# print(emp_data.loc[(emp_data.Name=='Maryam') & (emp_data.Salary>=20000)]) #for multiple conditions

#method two
# print(emp_data.iloc[2]) #for single row
# print(emp_data.iloc[1:3]) #for multiple rows slicing





