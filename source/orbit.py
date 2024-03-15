import numpy as np
from physics import Physics


class Orbit():
    def __init__(self):
        self._p = Physics()


    def eccentricity(self, velocity, relative, angular_momentum, k):
        e = (np.cross(velocity, angular_momentum) / k) - (relative / self._p.mag(relative))
        return e

    def inclination(self, angular_momentum):
        q = angular_momentum[2] / self._p.mag(angular_momentum)
        return np.arccos(q)

    def node(self, angular_momentum):
        N = np.cross(np.array([0,0,1]), angular_momentum)
        return N
    
    def ascention_node(self, N):
        if self._p.mag(N) == 0:
            Omega = 0
        elif N[1]>= 0:
            Omega = np.arccos(N[0] / self._p.mag(N))
        elif N[1] < 0:
            Omega = 2 * np.pi - np.arccos(N[0] / self._p.mag(N))
        
        return Omega

    def periapsis(self, ascention_node, eccentricity):
        Necc = np.dot(ascention_node, eccentricity)
        ne = self._p.mag(ascention_node) * self._p.mag(eccentricity)

        if ne == 0:
            periapsis = np.arctan2(eccentricity[1], eccentricity[0])
        elif eccentricity[2] >= 0:
            periapsis = np.arccos(Necc,ne)
        else:
            periapsis = 2*np.pi - np.arccos(Necc / ne)
        
        return periapsis
    
    def true_anomaly(self, eccentricity, relative, radial_velocity):
        eccr = np.dot(eccentricity, relative)
        er = self._p.mag(eccentricity) * self._p.mag(relative)

        if radial_velocity >= 0:
            theta = np.arccos(eccr / er)
        elif radial_velocity < 0:
            theta = 2 * np.pi - np.arccos(eccr / er)
        
        return theta


if __name__ == "__main__":
    pass