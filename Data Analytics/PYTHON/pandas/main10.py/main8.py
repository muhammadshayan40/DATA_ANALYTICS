#Aggeregation and Grouping
#isse counts kr skte hn, sum kr skte hn, mean kr skte hn, max min kr skte hn
import pandas as pd

data={
    'Name' : ["Shayan", "Ali", "Sara" ,"Maryam"],
    'Age':[19,20,20,18],
    'Salary':[55000, 40000, 45000, 60000]
}

emp_data=pd.DataFrame(data)

print(emp_data['Age'].value_counts())#yeh count krta hn ki kaunse age kitni baar ah rhi hn
print(emp_data[emp_data['Age']==18].value_counts())# isse 18 wali value dega

#GROUPING GPT SE KRLENA