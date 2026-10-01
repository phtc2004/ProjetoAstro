class CelestialBody:
    def __init__(self, name, radius_km, mass_kg, gravity):
        self.name = name
        self.radius_km = radius_km
        self.mass_kg = mass_kg
        self.gravity = gravity

    def resume(self):
        return f"{self.name}: radius = {self.radius_km} km | Mass = {self.mass_kg} kg | Gravity = {self.gravity} m/s²"


class Atmosphere:
    def __init__(self, pressure, composition):
        self.pressure = pressure
        self.composition = composition


class Planet(CelestialBody):
    def __init__(
        self,
        name,
        radius_km,
        mass_kg,
        gravity,
        orbital_period_days,
        avg_temp,
        atmosphere=None,
    ):
        super().__init__(name, radius_km, mass_kg, gravity)
        self.orbital_period_days = orbital_period_days
        self.avg_temp = avg_temp
        self.atmosphere = atmosphere

    def resume(self):
        base_resume = super().resume()
        planet_resume = f"{base_resume} | O_P_D = {self.orbital_period_days} | AVG_temp = {self.avg_temp}"
        if self.atmosphere is not None:
            planet_resume += f' | Atmosphere Composition: {self.atmosphere.composition}'
        return planet_resume


earth_atmosphere = Atmosphere(
    1, {"N2": 0.7808, "O2": 0.2095, "Ar": 0.0093, "CO2": 0.0004, "Others": 0.0}
)

earth = Planet("Earth", 6371, 6.973e24, 9.807, 365.256, 15.1, earth_atmosphere)


print(earth.name)
print(earth.resume())
