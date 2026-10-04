import math

from ursina import Entity, time, Mesh, PointLight
from ursina.shaders import lit_with_shadows_shader
from visual_scaling import *
from star import Star

class CelestialBody3D:

    def __init__(self, celestial_body, texture, orbiting_3d=None):
        self.celestial_body = celestial_body
        self.texture = texture
        self.orbiting_3d = orbiting_3d
        self.entity = Entity(
            model="sphere",
            scale=visual_scale(self.celestial_body),
            texture=self.texture,
        )

        self.rotation_speed = visual_rotation_speed(self.celestial_body)

        self.orbit_angle = 0

        if not isinstance(self.celestial_body, Star):
            self.orbit_radius = visual_distance(self.celestial_body)
            self.orbit_speed = visual_orbit_speed(self.celestial_body)
            self.entity.shader = lit_with_shadows_shader
        else:
            self.orbit_radius = 0
            self.orbit_speed = 0
            self.light = PointLight(position=self.entity.position)

        self.create_orbit_line()

    def rotate(self):
        self.entity.rotation_y += self.rotation_speed * time.dt

    def orbit(self):
        if not isinstance(self.celestial_body, Star):
            self.orbit_angle += self.orbit_speed * time.dt
            x = self.orbiting_3d.entity.position[0] + self.orbit_radius * math.cos(self.orbit_angle)
            z = self.orbiting_3d.entity.position[2] + self.orbit_radius * math.sin(self.orbit_angle)
            self.entity.position = (x, 0, z)
            self.orbit_entity.position = self.orbiting_3d.entity.position

    def create_orbit_line(self):
        if not isinstance(self.celestial_body, Star):
            points = 50
            self.orbit_line = []
            for a in range(points + 1):
                angle = a * (2*math.pi / points)
                x = self.orbit_radius * math.cos(angle)
                z = self.orbit_radius * math.sin(angle)
                self.orbit_line.append((x, 0, z))
            self.orbit_mesh = Mesh(vertices=self.orbit_line, mode="line")
            self.orbit_entity = Entity(model=self.orbit_mesh)
