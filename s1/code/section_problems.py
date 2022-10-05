import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.integrate import quad
print("Defining sin function")

sin = np.sin

print("minimizing sin function")
res = minimize(sin, [0], method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
print("Minimum res.x)

print("Integrating sin from 0 to 1 using scipy")
I = quad(sin, 0, 1)
print("Integral of sin from x=0..1: {}".format(I[0]))

print("Plotting from 0 to 2pi")
x = np.linspace(0, 2*np.pi, 200)
plt.plot(x, sin(x))
plt.xlabel("data[0]")
plt.ylabel("Count")
plt.show()
