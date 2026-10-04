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
        self.root_entity = Entity()
        self.tilt_entity = Entity(
            parent=self.root_entity, rotation_z=self.celestial_body.axial_tilt_degrees
        )
        self.entity = Entity(
            parent=self.tilt_entity,
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
            x = self.orbiting_3d.root_entity.position[0] + self.orbit_radius * math.cos(
                self.orbit_angle
            )
            z = self.orbiting_3d.root_entity.position[2] + self.orbit_radius * math.sin(
                self.orbit_angle
            )
            self.root_entity.position = (x, 0, z)
            self.orbit_entity.position = self.orbiting_3d.root_entity.position

    def create_orbit_line(self):
        if not isinstance(self.celestial_body, Star):
            points = 50
            self.orbit_line = []
            for a in range(points + 1):
                angle = a * (2 * math.pi / points)
                x = self.orbit_radius * math.cos(angle)
                z = self.orbit_radius * math.sin(angle)
                self.orbit_line.append((x, 0, z))
            self.orbit_mesh = Mesh(vertices=self.orbit_line, mode="line")
            self.orbit_entity = Entity(model=self.orbit_mesh)

    def create_rings(self, inner_radius, outer_radius, texture):
        points = 64
        vertices = []
        uvs = []
        for a in range(points + 1):
            angle = a * (2 * math.pi / points)

            inner_x = inner_radius * math.cos(angle)
            inner_z = inner_radius * math.sin(angle)

            outer_x = outer_radius * math.cos(angle)
            outer_z = outer_radius * math.sin(angle)

            vertices.append((inner_x, 0, inner_z))
            vertices.append((outer_x, 0, outer_z))

            v = a / points
            uvs.append((0, v))
            uvs.append((1, v))

        triangles = []
        for i in range(points):
            current_inner = i * 2
            current_outer = i * 2 + 1

            next_inner = (i + 1) * 2
            next_outer = (i + 1) * 2 + 1

            triangles.append((current_inner, current_outer, next_inner))
            triangles.append((current_outer, next_outer, next_inner))
        ring_mesh = Mesh(vertices=vertices, triangles=triangles, uvs=uvs)
        self.rings_entity = Entity(parent=self.tilt_entity, model=ring_mesh, texture=texture)
