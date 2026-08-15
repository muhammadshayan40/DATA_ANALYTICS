# datetime, Random ,Math
import datetime
x = datetime.datetime.now() #current time & date
print(x)

y= datetime.datetime(2020, 5 , 27)
print(y.strftime("%Y")) # Year with century as a decimal number
print(y.strftime("%y")) # Year without century as a decimal number
print(y.strftime("%m")) # Month as a decimal number

# 3-------------------------------------------------------------
import random

c= random.randint(1,6) # random number b/w 1-6
print (c)

list=["Heads", "Tails"]
d=random.choice(list)
print(d)

#____________________________________________________

import math

#i know this