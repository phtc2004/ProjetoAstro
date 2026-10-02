from planet import Planet
from orbit import Orbit
from star import Star
from moon import Moon
from atmosphere import Atmosphere


earth_atmosphere = Atmosphere(1, {'N2':0.7808, 'O2':0.2095, 'Ar':0.0093, 'CO2':0.0004, 'Others':0.0})
earth_orbit = Orbit(149597870.7, 365.256, 29.78)
earth = Planet('Earth', 6371, 6.973e24, 9.807, 15.1, earth_atmosphere, earth_orbit)
print(earth.resume())

sun = Star("Sun", 696000.0, 1.989e30, 274.0, "G2V", 5778, {"H": 0.7346, "He": 0.2485, "O": 0.0077}, 1.0)
print(sun.resume())

moon_orbit = Orbit(384400.0, 27.322, 1.022)
moon = Moon("Moon", 1737.4, 7.342e22, 1.62, moon_orbit)
print(moon.resume())
