import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from scipy.optimize import fmin
def function (x,y):

	return x**2-y**2



x = np.linspace(-400, 400, 100)
y = np.linspace(-400, 400, 100)
X, Y = np.meshgrid(x, y)
Z = function(X,Y)
fig = plt.figure(figsize = (10,7))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=5, cstride=5,
                cmap='cool')
ax.set_title("Task2", fontsize = 13)
ax.set_xlabel('x', fontsize = 11)
ax.set_ylabel('y', fontsize = 11)
ax.set_zlabel('Z', fontsize = 11)
plt.show()


