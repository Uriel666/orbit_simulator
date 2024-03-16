import numpy as np
from body import Body

class Physics(Body):
    def __init__(self, mass, position, velocity):
        self._G = 6.67e-11                             # Gravitational constant (N m2 / kg2)
        Body.__init__(self, mass, position, velocity)


    @property
    def p(self):
        return self._mass * self._velocity
    
    @property
    def L(self):
        return np.cross(self._position , self._velocity)
    
    @property
    def E(self):
        k = self._G*self._mass
        E = (1/2)*(self.mag_velocity**2) - k/self.mag_position
        return E

    # @property
    # def vr(self):
    #     return np.dot(self._position, self._velocity) / self.mag_position
    
    # @property
    # def vtheta(self):
    #     L = np.cross(self._position , self._velocity)
    #     return np.dot(L, L) / self.mag_position**2
        


if __name__ == "__main__":
    object = Physics(1e3, np.array([1,1,1]), np.array([4,5,6]))
    print(object.L)