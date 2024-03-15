import numpy as np
from physics import Physics
from body import Body

p = Physics()

G = 6.67e-11                          # Gravity constant (N m**2 / kg**2)
M = 5.972e24
m = 1e3                          # Earth mass (kg)

b1 = Body(m, np.array([1,1,1]), np.array([2,3,4]))
b2 = Body(M, np.array([0,0,0]), np.array([0,0,0]))

k = G * (b1.mass + b2.mass)   # Inertia constant


r = b1.position - b2.position
v = b1.velocity - b2.velocity


magr = p.mag(r)

print(magr)