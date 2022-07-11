# Welcome to the velocity calculator. Please enter the following:

# Mass (in kg): 5
# Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): 9.8
# Time (in seconds): 10
# Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): 1.3
# Cross sectional area (in m^2): 0.01
# Drag constant (0.5 for sphere, 1.1 for cylinder): 0.5

# The inner value of c is: 0.003
# The velocity after 10.0 seconds is: 67.512 m/s
# math.sqrt(m * g/c) * (1 - exp((-math.sqrt(mgc)/m)t))

import math
print('Welcome to the velocity calculator. Please enter the following: \n')
m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

c = .5 * (p * A * C)
exponent = ((-(math.sqrt(m * g * c))/m)* t)
v = math.sqrt(((m * g)/c)) * (1 - math.exp(exponent))

print(f'The inner value of c is: {c:.3f}')
print(f'The velocity after 10 seconds is: {v:.3f}')