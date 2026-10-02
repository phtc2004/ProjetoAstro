class CelestialBody:

    def __init__(self, name, radius_km, mass_kg, gravity):
        self.name = name
        self.radius_km = radius_km
        self.mass_kg = mass_kg
        self.gravity = gravity

    def resume(self):
        return f"{self.name}: radius = {self.radius_km} km | Mass = {self.mass_kg} kg | Gravity = {self.gravity} m/s²"