from numpy import array, sqrt, pi, sin, cos, arctan, tan
from Tools import mag


class EllipticIntegrator():

    def __init__(self):
        pass


    def MeanAnomalyTime(self, Me0, T, time):
        return Me0 + ((2*pi) / T) * time
    
    def EccentricAnomalyTime(self, Me, e):
        if Me < pi:
            E = Me + e/2
        else:
            E = Me - e/2
        
        ratio = 1
        total_error = 1e-8

        while abs(ratio)>total_error:
            ratio = (E - e * sin(E) - Me) / (1-e*cos(E))
            E = E - ratio  
        return E
    
    def TrueAnomalyTime(self, E, e):
        return 2 * arctan( sqrt( (1+e) / (1-e) ) * tan(E / 2) )
    
    def PerifocalState(self, Me0, e, k, L, T, time):
        Me = self.MeanAnomalyTime(Me0, T, time)
        E = self.EccentricAnomalyTime(Me , mag(e))
        theta = self.TrueAnomalyTime(E, mag(e))

        rp = (mag(L)**2 / k) * (1 / (1+mag(e)*cos(theta))) * cos(theta)
        rq = (mag(L)**2 / k) * (1 / (1+mag(e)*cos(theta))) * sin(theta)
        rz = (mag(L)**2 / k) * (1 / (1+mag(e)*cos(theta))) * 0

        vp = (k / mag(L)) * (-sin(theta))
        vq = (k / mag(L)) * (mag(e) + cos(theta))
        vz = (k / mag(L)) * 0

        return array([rp,rq,rz]), array([vp, vq, vz])