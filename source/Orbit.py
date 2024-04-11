from Physics import Physics
from numpy import cross, array, dot, sqrt, arctan, tan, sin, arccos, pi, arctan2
from Tools import mag

class EllipticalOrbitalElements(Physics):
    def __init__(self, mass, initial_position, initial_velocity):
        super().__init__(mass, initial_position, initial_velocity)

        self._L = self.AngularMomentum()
        self._E = self.Energy()
    
    def SemiMajorAxis(self):
        return -(self._k / (2*self._E))
    
    def EccentricVector(self):
        return (cross(self._velocity, self._L) / self._k) - (self._position / mag(self.position))
    
    def Period(self):
        a = self.SemiMajorAxis()
        return (2*pi / (sqrt(self._k)) ) * (a**(3/2))
    
    def TrueAnomaly(self):
        vr = self.RadialVelocity()
        e = self.EccentricVector()

        angle = arccos( dot(e, self._position) / (mag(self._position) * mag(e)) )

        if vr >= 0:
            return angle
        elif vr < 0:
            return 2*pi - angle


    def Inclination(self):
        return arccos(self._L[2] / mag(self._L))
    
    def NodeVector(self):
        return cross(array([0,0,1]), self._L)
    
    def AscentionNode(self):
        N = self.NodeVector()
        angle = arccos(N[0] / mag(N))

        if mag(N) == 0:
            return 0
        elif N[1] >= 0:
            return angle
        elif N[1]<0:
            return 2*pi - angle

    def PeriapsisArgument(self):
        e = self.EccentricVector()
        N = self.NodeVector()

        Ne = dot(N, e)
        ne = mag(N) * mag(e)

        angle = arccos(Ne / ne)

        if ne == 0:
            return arctan2(e[1] / e[0])
        elif e[2] >= 0:
            return angle
        else:
            return 2*pi - angle
    

    def EccentricAnomaly(self):
        theta = self.TrueAnomaly()
        e = self.EccentricVector()
        return 2*arctan(sqrt((1-mag(e)) / (1+mag(e))) * tan(theta / 2))
    
    def MeanAnomaly(self):
        E = self.EccentricAnomaly()
        e = self.EccentricVector()
        return E - mag(e)*sin(E)
