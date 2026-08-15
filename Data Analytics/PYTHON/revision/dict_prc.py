# Problem Solving:

# 1.Write a python program to sort a dictionary by value.
x={"b": 3, "c":65, "d": 34, "e": 23}

new_x=sorted(x.values())
print(new_x)

# 2.Write a python script to print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys.  
y={}

for i in range(1, 16):
    y[i]= i ** 2
print(y)

# 3.Write a program to multiply all the items in a dictionary. 
#use x dict from  above

mul=1
for i in x.values():
    mul= mul * i
    
print(mul)    


# 4.Write a python program to sort a dictionary by key.
t={"b": 3, "d": 34, "e": 23 ,"c":65}
new_t=sorted(t.keys())
print(new_t)
