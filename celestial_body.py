class CelestialBody:

    def __init__(self, name, radius_km, mass_kg, gravity, rotation_period_hours, axial_tilt_degrees):
        self.name = name
        self.radius_km = radius_km
        self.mass_kg = mass_kg
        self.gravity = gravity
        self.rotation_period_hours = rotation_period_hours
        self.axial_tilt_degrees = axial_tilt_degrees

    def resume(self):
        return f"{self.name}: radius = {self.radius_km} km | Mass = {self.mass_kg} kg | Gravity = {self.gravity} m/s²"