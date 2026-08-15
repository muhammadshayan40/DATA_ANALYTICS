

# -------------------------------------------------------.
#A = ["Ross", "Rachel", "Monica", "Joe"]
# Write a program to swap first and forth element.
x = ["Ross", "Rachel", "Monica", "Joe"]
print(x)
x[0],x[-1]=x[-1],x[0]
print(x)

#-----------------------------------------------------
# Write a program to add a new value at second position.
#for add at specific position we use insert method,bc append add to the last
y = [" Chandler", "Joey","shyn","why"]
print(y)
y.insert(1,"mrym")
print(y)

#----------------------------------------------
# Write a program to delete a value from 3rd position.
b=[13,6 ,89 ,45]
b.pop(2)
print(b)
#---------------------------------------------------
# Write a program to multiply all the numbers in the list.
mul=1
for i in range(len(b)):  # OR #for i in b:
    mul= mul * b[i]           #     mul= mul *i
    
print(mul)    
#--------------------------------------------------
# Write a program to get the largest , smallest number from the list
b.sort()
print(f"largest num is {b[-1]} & smallest num is {b[0]}")
#-----------------------------------------------------