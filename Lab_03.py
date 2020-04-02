import numpy as np
import matplotlib.pyplot as plt

# Viscosity Calculations (Pa*s)
R = 0.0035
P_avg = 1 / (0 - 0.065) * 0.5 * 1790 * 9.81 * -(0.065)**2
V_cup = 9.4e-5
t = 10.4
Q = V_cup / t
L = 0.005

eta = np.pi * R**4 * P_avg / (8 * Q * L)
print("Viscosity: ", eta, " Pa*s")

x = np.arange(0, 20, 0.1)
y = np.pi * R**4 * P_avg * x/ (8 * V_cup * L)
plt.plot(x, y)
plt.title('Viscosity vs. Time Graph')
plt.xlabel('Time (s)')
plt.ylabel('Viscosity (Pa*s)')
plt.show()

# Density Calculations (g/cm^3)
A = np.array([[197.5, 198, 198, 18.76, 19.30, 19.15, 9.51, 9.55,9.49],
              [199, 198, 198, 18.71, 19.99, 18.90, 9.46, 9.59, 9.31],
              [198, 197.5, 197.5, 19.13, 19.12, 19.19, 9.48, 9.63, 9.39],
              [199, 198.9, 199, 19.68, 19.10, 18.81, 9.53, 9.40, 10.03],
              [198, 199, 198, 19.08, 18.79, 19.25, 9.55, 9.67, 9.79],
              [197.5, 197, 197, 19.05, 18.94, 19.26, 9.62, 9.38, 9.53]])

m = np.array([60.05, 60.18, 60.34, 60.13, 59.86, 59.97])

A_avg = np.zeros((6, 3))
for i in range(0,6):
    for j in range(0,3):
        A_avg[i,j] = np.mean(A[i,(3*j):(3*j+3)])
        
V_bar = np.multiply(0.001, np.prod(A_avg, axis=1))

d = np.divide(m,V_bar)
d_B = np.mean(d)
d_std = np.std(d)
print("Average Bulk Density: ", d_B, " g/cm^3")
print("Density Standard Deviation: ",d_std, " g/cm^3")

# Porosity Calculations
d_T = 2.5

v = 1 - d_B / d_T
print("Void Fraction: ",v)

