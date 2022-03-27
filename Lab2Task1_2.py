#import modules
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from scipy.optimize import *
import math


#create picture using coordinate systems
fig=plt.subplots()
#space where will be presented our graph
x=np.linspace(-5,5,100)

#First let's plot our function
plt.plot(x,(x+(1/(exp(x-1)-1))))

plt.title("Lab2 Task1.2")
plt.ylabel("Y")
plt.xlabel("X")
plt.grid()
plt.show()

#Let's start optimization process
x = np.arange(-10, 10, 5000)
def f(x):
    return x+(1/(exp(x-1)-1))
    
print(minimize(lambda x: f(x), -1))
# Global optimization
grid = (-10, 10, 0.1)

# Constrain optimization
xmin_local = optimize.fminbound(f, 0, 10)
print("Local minimum found %s" % xmin_local)

