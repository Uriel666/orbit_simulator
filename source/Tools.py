from numpy import sqrt, dot


G = 6.67430e-11            # Nm^2 / kg^2 
EARTH_MASS = 5.972e24      # kg
EARTH_RADIUS = 6.371e6     # m
    

def mag(vector):
    return sqrt(dot(vector, vector))

if __name__ == "__main__":
    pass