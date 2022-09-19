"""
Created on Tue Sep  6 09:25:39 2022

@author: Richter
"""
import sys

print("> Welcome to the Python installation test script!")

print("If you are seen this message then Python {0}.{1} is installed in you computer:".format(sys.version_info[0], sys.version_info[1]))

print("> Let's check the other packages ...")

flag = True

try:
	import numpy as np
	print("The module Numpy {0} is installed!".format(np.__version__))
except e:
	print("ERROR: Numpy is not installed in the computer!")
	flag = False

try:
	import scipy
	from scipy.interpolate import CubicSpline
	print("The module Scipy {0} is installed!".format(scipy.__version__))
except e:
	print("ERROR: Scipy is not installed in the computer!")
	flag = False

try:
	import matplotlib
	import matplotlib.pyplot as plt
	print("The module Numpy {0} is installed!".format(matplotlib.__version__))
except e:
	print("ERROR: Matplotlib is not installed in the computer!")
	flag = False

if flag:
	print("Test finished successfully!")
else:
	print("There are problems with some of the modules. Try to re-install them.")
	sys.exit()


print("Hello World! numpy, scipy and matplotlib have been loaded. Let's play with them!")

x = np.linspace(0,10,7)
y = np.sin(x)

print('7 points from 0 to 10',x)
print('Sinus in these points',y)


cs = CubicSpline(x, y)


print('Now we plot the points and a smooth Spline-Interpolation')
print('You should see a plot!')

X = np.linspace(0,10,101)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.plot(x,y,'*')
plt.plot(X,cs(X),label='Cubic Spline')
plt.legend()
plt.show()
