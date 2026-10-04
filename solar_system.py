from planet import Planet
from orbit import Orbit
from star import Star
from moon import Moon
from atmosphere import Atmosphere

sun_object = Star(
    "Sun",
    696000.0,
    1.989e30,
    274.0,
    609.12,
    "G2V",
    5778,
    {"H": 0.7346, "He": 0.2485, "O": 0.0077},
    1.0,
)

earth_atmosphere = Atmosphere(
    1, {"N2": 0.7808, "O2": 0.2095, "Ar": 0.0093, "CO2": 0.0004, "Others": 0.0}
)
earth_orbit = Orbit(149597870.7, 365.256, 29.78, sun_object)
earth_object = Planet(
    "Earth", 6371, 6.973e24, 9.807, 23.9345, 15.1, earth_atmosphere, earth_orbit
)

moon_orbit = Orbit(384400.0, 27.322, 1.022, earth_object)
moon_object = Moon("Moon", 1737.4, 7.342e22, 1.62, 655.7, moon_orbit)

mercury_orbit = Orbit(57909227, 87.97, 47.36, sun_object)
mercury_object = Planet(
    "Mercury", 2439.7, 3.3011e23, 3.7, 1407.6, 167, orbit=mercury_orbit
)

venus_orbit = Orbit(108209475, 224.7, 35.02, sun_object)
venus_object = Planet(
    "Venus", 6051.8, 4.8675e24, 8.87, -5832.6, 464, orbit=venus_orbit
)

mars_orbit = Orbit(227943824, 686.98, 24.07, sun_object)
mars_object = Planet(
    "Mars", 3389.5, 6.4171e23, 3.71, 24.6229, -65, orbit=mars_orbit
)

jupiter_orbit = Orbit(778340821, 4332.59, 13.07, sun_object)
jupiter_object = Planet(
    "Jupiter", 69911, 1.8982e27, 24.79, 9.9250, -110, orbit=jupiter_orbit
)

saturn_orbit = Orbit(1426666422, 10759.22, 9.69, sun_object)
saturn_object = Planet(
    "Saturn", 58232, 5.6834e26, 10.44, 10.656, -140, orbit=saturn_orbit
)

uranus_orbit = Orbit(2870658186, 30688.5, 6.81, sun_object)
uranus_object = Planet(
    "Uranus", 25362, 8.6810e25, 8.69, -17.2, -195, orbit=uranus_orbit
)

neptune_orbit = Orbit(4498396441, 60182, 5.43, sun_object)
neptune_object = Planet(
    "Neptune", 24622, 1.02413e26, 11.15, 16.1, -200, orbit=neptune_orbit
)