import pandas as pd
#NEXT TOPIC => FILTER DATAFRAMES
#--------------------------------------
data={
    'Name' : ["Shayan", "Ali", "Sara" ,"Maryam"],
    'Age':[19,20,20,18],
    'Salary':[55000, 40000, 45000, 60000]
}

emp_data=pd.DataFrame(data)

# data_ageFILTER=emp_data[emp_data['Age']>18] #filtering dataframes
data_ageFILTER=emp_data[(emp_data['Age']>18) & (emp_data['Salary']>40000)] #for multiple conditions

print(data_ageFILTER)

#or new variable me save kr k hum un value ko ek separate daraframe me save kr skte hn

#=======================================================
#but where method is used to filter dataframes, it is used for multiple conditions
#or jahan value condition se match nhi hongi waha NaN value ahjati hn

print(emp_data.where(emp_data['Age']>18))

# #if u want to change the NaN text from where method, use "other"
# print(emp_data.where(emp_data['Age']>18),other="Not Matched")