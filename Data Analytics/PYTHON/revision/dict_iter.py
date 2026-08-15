Student_data = {"name": "David", "age":13, "marks":87}  

# for keys
for i in Student_data:
    print(i)

#for vlues    
for i in Student_data:
    print(Student_data[i])
    
for i in Student_data.values():
    print(i)

# for both
for x,y in Student_data.items():
    print(x,":",y)    
    
    