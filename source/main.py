import numpy as np
from physics import Physics
from body import Body

p = Physics()

G = 6.67e-11                          # Gravity constant (N m**2 / kg**2)
M = 5.972e24                          # Earth mass (kg)

b1 = Body(100, np.array([1,1,1]), np.array([2,3,4]))
b2 = Body(100, np.array([5,3,6]), np.array([4,5,6]))

k = G * (b1.mass + b2.mass)   # Inertia constant


r = b1.position - b2.position

magr = p.mag(r)

print(magr)