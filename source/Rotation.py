from numpy import array, cos, sin, dot

class GeocentricalRotations():

    def __init__(self) -> None:
        pass

    def PerifocalRotation(self, omega):
        return array([[cos(omega), sin(omega), 0], [-(sin(omega)), cos(omega), 0], [0,0,1] ])
    
    def InclinationRotation(self, i):
        return array([[1, 0, 0], [0, cos(i), sin(i)], [0,-(sin(i)),cos(i)]])
    
    def NodeRotation(self, Omega):
        return array([[cos(Omega), sin(Omega), 0], [-(sin(Omega)), cos(Omega), 0], [0,0,1] ])
    

    def TransformationMatrix(self, i, omega, Omega):
        Rom = self.PerifocalRotation(omega)
        Ri = self.InclinationRotation(i)
        ROM = self.NodeRotation(Omega)

        return dot(Rom, Ri, ROM)
    

    def EquatorialVector(self, vector, i, omega, Omega):
        Q = self.TransformationMatrix(i, omega, Omega)

        Q = Q.transpose()
        vector = vector.transpose()

        return dot(Q, vector)
    

if __name__ == "__main__":
    pass

