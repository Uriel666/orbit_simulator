import numpy as np
from physics import Physics


class Orbit():
    def __init__(self):
        self._p = Physics()

    def semi_major_axis(self, k, Energy):
        return -(k/(2*Energy))
    
    def period(self, k, semi_major_axis):
        T = ((2*np.pi) / np.sqrt(k)) * semi_major_axis**(3/2)
        return T

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
    
    def mean_anomaly(self, period, t):
        return ((2*np.pi) / period) * t
    
    def eccentric_anomaly(self, mean_anomaly, eccentricity):
        if mean_anomaly< np.pi:
            E = mean_anomaly + eccentricity/2
        else:
            E = mean_anomaly - eccentricity/2
        
        ratio = 1
        total_error = 1e-8

        while abs(ratio) > total_error:
            ratio = (E - eccentricity * np.sin(E) - mean_anomaly) / (1 - eccentricity * np.cos(E))
            E = E - ratio
        
        return E
    
    def perifocal_rotation(self, periapsis):
        Rom = np.array([[np.cos(periapsis), np.sin(periapsis), 0], [-(np.sin(periapsis)), np.cos(periapsis), 0], [0,0,1]])
        return Rom


if __name__ == "__main__":
    pass