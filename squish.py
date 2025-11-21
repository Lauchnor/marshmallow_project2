import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("mello_table.csv", delimiter=",", dtype=str)

x = data[1:, 0].astype(np.float32)
y = data[1:, 1].astype(np.float32)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

###Exercise 1
print_equation(slope, intercept, 'cm', 'g')
#Equation of the line: y = -0.004121428572134348 cm/g x + 5.842500000399565 cm


###Exercise 2
plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') 
plt.legend(loc='best')
plt.xlabel("Weight(Grams)") 
plt.ylabel("Distance in x direction (Centimeters)") 
plt.show()
