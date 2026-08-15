#line plot

import matplotlib.pyplot as plt

days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
week1=[17,213,340,40,150,260,470]#customer data for week 1
week2=[65,150,250,555,10,300,700]#customer data for week 2

plt.plot(days,week1, label="week1", color="green", marker="o")
plt.plot(days,week2, label="week2", color="blue", marker="s")
plt.legend()

plt.show()