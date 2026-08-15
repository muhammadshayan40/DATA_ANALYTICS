
# Level 1 – Variables, Input, Operators (10 Questions)

# User se naam aur age lo aur print karo:

# Hello Shayan, you are 21 years old.
# User se 2 numbers lo aur unka:
# Sum
# Difference
# Product
# Division print karo.
# Celsius ko Fahrenheit me convert karo.
# Rectangle ka area aur perimeter calculate karo.
# Circle ka area calculate karo (π = 3.1416).
# User se 5 subject marks lo aur percentage calculate karo.
# Seconds ko Hours, Minutes, Seconds me convert karo.
# Swap two numbers (without using third variable).
# Even ya Odd check karo.
# Number positive, negative ya zero hai, check karo.

#________________________________________________
#__________________SOLUTIONS______________________
#

# name=input("Enter your name:")
# age=input("Enter your age:")

# print(f"Hello {name}, you are {age} years old.")

#______________________


# num1=float(input("Enter first number: "))
# num2=float(input("Enter second number: "))

# sum=num1+num2
# difference=num1-num2
# product=num1*num2
# division=num1/num2

# print(f"Sum: {sum}")
# print(f"Difference: {difference}")
# print(f"Product: {product}")
# print(f"Division: {division}")

#______________________

# C=float(input("Enter temperature in Celsius: "))

# F=(C*9/5)+32

# print(f"Temperature in fahrenhite is: {F}")

#______________________

# l=int(input("Enter lenght: "))
# w=int(input("Enter width: "))

# area=l*w
# perimeter=2*(l+w)

# print(area)
# print(perimeter)

#______________________

# d=int(input("Enter diameter of Circle: "))
# r=d/2

# area=3.14*pow(r,2)
# print(f"The area of Circle is {area}")

#______________________

# marks=[]
# subjects=int(input("Enter number of subjects: "))

# for i in range(subjects):
#     mark=int(input(f"Enter marks of subject {i+1}: "))
#     marks.append(mark)

# total_mk=subjects*100
# total_obt=sum(marks)

# percentage=(total_obt/total_mk)*100
# print(f"Your Percentage is {percentage}%")    

#______________________

# seconds=int(input("Enter seconds:"))

# hours=seconds/3600
# minutes=(seconds%3600)/60
# secs=seconds%60

# print(f"Time: {hours:.0f}:{minutes:.0f}:{secs:.0f}")

#______________________

# print("Before swapping: ")
# x=int(input("Enter 1st number: "))
# y=int(input("Enter 2nd number: \n"))

# x,y=y,x
# print(f"After swapping: {x}, {y}")

#______________________

# num=int(input("Enter a number"))

# if num%2==0:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")    
    
#________________________

# num=int(input("Enter a number: "))

# if(num>0):
#     print(num," is positive")
# elif(num<0):
#     print(num," is negative")        
# elif num==0:
#     print(num," is zero")
# else:
#     print("Invalid input")            

#_______________________________________