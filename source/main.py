import numpy as np
from physics import Physics
from body import Body
from orbit import Orbit

m1 = 5.972e24
m2 = 1e3

b1 = Body(m1, np.array([0,0,0]), np.array([0,0,0]))
b2 = Body(m2, np.array([1,1,1]), np.array([2,3,4]))
o = Orbit()

M = (b1.mass + b2.mass)
r = b2.position - b1.position
v = b2.velocity - b1.velocity
R = (b1.mass*b1.position * b2.mass * b2.position)/M

v_body = Physics(M, r, v)

print(v_body.p)