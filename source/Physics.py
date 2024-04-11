from numpy import cross, dot
from Tools import G, EARTH_MASS, mag


class Physics():

    def __init__(self, mass, initial_position, initial_velocity):
        self._m = mass
        self._position = initial_position
        self._velocity = initial_velocity
        self._k = G * (EARTH_MASS + self._m)
    


    @property
    def k(self):
        return self._k    

    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, new_postion):
        self._position = new_postion
    
    @property
    def velocity(self):
        return self._position
    
    @velocity.setter
    def position(self, new_velocity):
        self._velocity = new_velocity

    def AngularMomentum(self):
        return cross(self._position, self._velocity)
    
    def Energy(self):
        T = (1/2) * (mag(self._velocity)**2)
        U = - (self._k / mag(self._position))

        return T + U
    
    def RadialVelocity(self):
        return dot(self._velocity, self._position) / (mag(self._position))

    def AngularVelocity(self):
        L = self.Energy()
        return mag(L) / (mag(self._position)**2)
    



if __name__ == "__main__":
    print("Hi")
