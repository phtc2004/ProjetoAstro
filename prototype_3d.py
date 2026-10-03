from ursina import *

app = Ursina()

sun = Entity(model="sphere", scale=2, position=(0, 0, 0), texture="textures/sun.jpg")
earth = Entity(model="sphere", scale=0.5, texture="textures/earth.jpg")
moon = Entity(model="sphere", scale=0.1, texture="textures/moon.jpg")

orbit_angle_earth = 0
earth_orbit_speed = 0.5
earth_orbit_radius = 5

orbit_angle_moon = 0
moon_orbit_speed = earth_orbit_speed * 5
moon_orbit_radius = 0.75

# Orbit lines

points = 50

orbit_line_earth = []
orbit_line_moon = []

for a in range(points):
    angle = a * (2*pi / points)
    e1 = earth_orbit_radius * cos(angle)
    e3 = earth_orbit_radius * sin(angle)
    m1 = moon_orbit_radius * cos(angle)
    m3 = moon_orbit_radius * sin(angle)
    orbit_line_earth.append((e1, 0, e3))
    orbit_line_moon.append((m1, 0, m3))

orbit_line_earth.append(orbit_line_earth[0])
orbit_line_moon.append(orbit_line_moon[0])

earth_lines_mesh = Mesh(vertices=orbit_line_earth, mode="line")
moon_lines_mesh = Mesh(vertices=orbit_line_moon, mode="line")

earth_orbit = Entity(model=earth_lines_mesh)
moon_orbit = Entity(model=moon_lines_mesh)
    
def update():

    global orbit_angle_earth, orbit_angle_moon

    sun.rotation_y += 2 * time.dt
    earth.rotation_y += 50.9 * time.dt
    moon.rotation_y += 13.2 * time.dt
    
    orbit_angle_earth += earth_orbit_speed * time.dt
    x_earth = earth_orbit_radius * cos(orbit_angle_earth)
    z_earth = earth_orbit_radius * sin(orbit_angle_earth)
    earth.position = (x_earth, 0, z_earth)
    moon_orbit.position = earth.position

    orbit_angle_moon += moon_orbit_speed * time.dt
    x_moon = x_earth + moon_orbit_radius * cos(orbit_angle_moon)
    z_moon = z_earth + moon_orbit_radius * sin(orbit_angle_moon)
    moon.position = (x_moon, 0, z_moon)

EditorCamera()
app.run()
