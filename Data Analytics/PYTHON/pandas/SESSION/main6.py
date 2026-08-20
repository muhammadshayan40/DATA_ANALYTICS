#ROW & CLOMS pr OPEERATIONS add wagera
import pandas as pd
data={
    'Name' : ["Shayan", "Ali", "Sara" ,"Maryam"],
    'Age':[19,20,20,18],
    'Salary':[55000, 40000, 45000, 60000]
}

emp_data=pd.DataFrame(data)
#print(emp_data)

#add new colms
emp_data['Team_ROLE']=['Analyst','Scientist','Engineer','Architect']
emp_data['Bonus']=emp_data['Salary']*0.2
#print(emp_data)

#adding rows

emp_data.loc[len(emp_data)]=["Rohit",19,75000, "Manager",75000*0.2]
print(emp_data)

#Update value

#BY USING INDEX
emp_data.loc[0, 'Salary'] = 90000

#BY COLM NAME
emp_data.loc[emp_data.Name=="Shayan", 'Salary'] = 90000
print(emp_data)

#delete row 
emp_data.drop(1, axis=0 ,inplace=True ) #index number, axis nah bhi liko toh koi problem nhi hn
print(emp_data)

#delete colm
emp_data.drop(['Bonus', 'Team_ROLE'], axis=1, inplace=True)
print(emp_data)


#SORTING VALUES
emp_data.sort_values('Salary', ascending=False)
print(emp_data)