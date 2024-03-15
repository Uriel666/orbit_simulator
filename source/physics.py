import numpy as np

class Physics():
    def __init__(self):
        pass

    def linear_momentum(self, mass, velocity):
        return mass * velocity

    def angular_momentum(self, position, velocity):
        return np.cross(position, velocity)
    
    def energy(self, mag_velocity, mag_position, k):
        E = 1/2 * (mag_velocity**2) - (k / mag_position)
        return E
    
    def angular_velocity(self, angular_momentum, mag_position):
        return np.dot(angular_momentum, angular_momentum) / mag_position**2

    def radial_velocity(self, position, velocity, mag_position):
        return np.dot(position, velocity) / mag_position
    
    
    def mag(self, a):
        return np.sqrt(np.dot(a,a))


if __name__ == "__main__":
    pass