from planet import Planet
from orbit import Orbit
from star import Star
from moon import Moon
from data.planet_data import *
from data.star_data import *
from data.moon_data import *

sun_object = Star(**SUN_DATA)


earth_orbit = Orbit(**EARTH_ORBIT_DATA, orbiting=sun_object)
earth_object = Planet(**EARTH_DATA, orbit=earth_orbit)

moon_orbit = Orbit(**MOON_ORBIT_DATA, orbiting=earth_object)
moon_object = Moon(**MOON_DATA, orbit=moon_orbit)


mercury_orbit = Orbit(**MERCURY_ORBIT_DATA, orbiting=sun_object)
mercury_object = Planet(**MERCURY_DATA, orbit=mercury_orbit)

venus_orbit = Orbit(**VENUS_ORBIT_DATA, orbiting=sun_object)
venus_object = Planet(**VENUS_DATA, orbit=venus_orbit)

mars_orbit = Orbit(**MARS_ORBIT_DATA, orbiting=sun_object)
mars_object = Planet(**MARS_DATA, orbit=mars_orbit)


jupiter_orbit = Orbit(**JUPITER_ORBIT_DATA, orbiting=sun_object)
jupiter_object = Planet(**JUPITER_DATA, orbit=jupiter_orbit)

io_orbit = Orbit(**IO_ORBIT_DATA, orbiting=jupiter_object)
io_object = Moon(**IO_DATA, orbit=io_orbit)

europa_orbit = Orbit(**EUROPA_ORBIT_DATA, orbiting=jupiter_object)
europa_object = Moon(**EUROPA_DATA, orbit=europa_orbit)

ganymede_orbit = Orbit(**GANYMEDE_ORBIT_DATA, orbiting=jupiter_object)
ganymede_object = Moon(**GANYMEDE_DATA, orbit=ganymede_orbit)

callisto_orbit = Orbit(**CALLISTO_ORBIT_DATA, orbiting=jupiter_object)
callisto_object = Moon(**CALLISTO_DATA, orbit=callisto_orbit)


saturn_orbit = Orbit(**SATURN_ORBIT_DATA, orbiting=sun_object)
saturn_object = Planet(**SATURN_DATA, orbit=saturn_orbit)

uranus_orbit = Orbit(**URANUS_ORBIT_DATA, orbiting=sun_object)
uranus_object = Planet(**URANUS_DATA, orbit=uranus_orbit)

neptune_orbit = Orbit(**NEPTUNE_ORBIT_DATA, orbiting=sun_object)
neptune_object = Planet(**NEPTUNE_DATA, orbit=neptune_orbit)
