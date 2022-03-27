#import modules
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import *
import math
#our function
#create picture using coordinate systems
fig=plt.subplots()
#space where will be presented our graph
x=np.linspace(-1.5,1.5,5000)

plt.plot(x,((x**6)/6)-(x**3)+(2*x))

def f(x):
	return ((x[0]**6)/6)-(x[0]**3)+(2*x[0])
#fmin(f,np.array([0,0]))
print(minimize(lambda x: f(x), -1))

plt.title("Lab2 Task1.1")
plt.ylabel("Y")
plt.xlabel("X")
plt.grid()
plt.show()