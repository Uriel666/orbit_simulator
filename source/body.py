import numpy as np

class Body():
    def __init__(self, mass, position, velocity):
        self._mass = mass
        self._position = position
        self._velocity = velocity

    
    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, new_mass):
        self._mass = new_mass

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, new_position):
        self._position = new_position
    
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self, new_velocity):
        self._velocity = new_velocity
    
    @property
    def mag_position(self):
        return np.sqrt(np.dot(self._position, self._position))
    
    @property
    def mag_velocity(self):
        return np.sqrt(np.dot(self._velocity, self._velocity))


if __name__ == "__main__":
    body1 = Body(1,2,3)
    body2 = Body(1,5,6)
    print(body1.position - body2.position)
