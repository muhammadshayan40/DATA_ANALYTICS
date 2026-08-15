#SCATETER CHART
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1,10,50)
y = np.random.randint(1,100,50)
plt.scatter(x, y,marker='o',color='red')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()