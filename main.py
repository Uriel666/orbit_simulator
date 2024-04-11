from numpy import linspace, array, pi, outer, sin , cos, ones, size
from source.Integrators import EllipticIntegrator
from source.Orbit import EllipticalOrbitalElements
from source.Rotation import GeocentricalRotations
from source.Tools import EARTH_RADIUS
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d
import matplotlib as mpl

if __name__ == "__main__":
    m = 5e3
    r0 = array([1.2*EARTH_RADIUS,1.2*EARTH_RADIUS,1.2*EARTH_RADIUS])
    v0 = array([-3200, 4500, 4500])

    orbit = EllipticalOrbitalElements(m, r0, v0)
    integrator = EllipticIntegrator()
    rot = GeocentricalRotations()

    theta0 = orbit.TrueAnomaly()
    L = orbit.AngularMomentum()
    T = orbit.Period()
    Me0 = orbit.MeanAnomaly()
    e = orbit.EccentricVector()
    k = orbit.k
    i = orbit.Inclination()
    omega = orbit.PeriapsisArgument()
    Omega = orbit.AscentionNode()

    time_range = linspace(0, T, 50)

    state_vectors = []

    for t in time_range:
        r_perifocal, v_perifocal = integrator.PerifocalState(Me0, e, k, L, T, t)
        r = rot.EquatorialVector(r_perifocal, i, omega, Omega)
        v = rot.EquatorialVector(v_perifocal, i, omega, Omega)

        state = (r,v,t)

        state_vectors.append(state)




    fig = plt.figure()
    ax = fig.add_subplot(projection = '3d')
    u = linspace(0, 2 * pi, 80)
    v = linspace(0, pi, 80)
    x = EARTH_RADIUS * outer(cos(u), sin(v))
    y = EARTH_RADIUS * outer(sin(u), sin(v))
    z = EARTH_RADIUS * outer(ones(size(u)), cos(v))
    ax.contour3D(x,y,z)

    for state in state_vectors:
        ax.scatter3D(state[0][0],state[0][1],state[0][2])
    
    mpl.rcParams['path.simplify'] = True

    ax.set_aspect('equal')

    plt.show()
