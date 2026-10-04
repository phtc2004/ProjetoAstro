from ursina import *
from solar_system import *
from celestial_body3d import CelestialBody3D


app = Ursina()
sky = Sky(texture="textures/stars.jpg")


sun_3d = CelestialBody3D(sun_object, "textures/sun.jpg")
earth_3d = CelestialBody3D(earth_object, "textures/earth.jpg", sun_3d)
moon_3d = CelestialBody3D(moon_object, "textures/moon.jpg", earth_3d)
mercury_3d = CelestialBody3D(mercury_object, "textures/mercury.jpg", sun_3d)
venus_3d = CelestialBody3D(venus_object, "textures/venus.jpg", sun_3d)
mars_3d = CelestialBody3D(mars_object, "textures/mars.jpg", sun_3d)
jupiter_3d = CelestialBody3D(jupiter_object, "textures/jupiter.jpg", sun_3d)
saturn_3d = CelestialBody3D(saturn_object, "textures/saturn.jpg", sun_3d)
uranus_3d = CelestialBody3D(uranus_object, "textures/uranus.jpg", sun_3d)
neptune_3d = CelestialBody3D(neptune_object, "textures/neptune.jpg", sun_3d)


orbiting_bodies = [
    earth_3d,
    moon_3d,
    mercury_3d,
    venus_3d,
    mars_3d,
    jupiter_3d,
    saturn_3d,
    uranus_3d,
    neptune_3d,
]

def update():
    sun_3d.rotate()

    for body in orbiting_bodies:
        body.rotate()
        body.orbit()


EditorCamera()
app.run()
