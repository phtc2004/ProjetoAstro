from celestial_body import CelestialBody

class Planet(CelestialBody):

    def __init__(
        self,
        name,
        radius_km,
        mass_kg,
        gravity,
        rotation_period_hours,
        avg_temp_celsius,
        atmosphere=None,
        orbit=None
    ):
        super().__init__(name, radius_km, mass_kg, gravity, rotation_period_hours)
        self.avg_temp_celsius = avg_temp_celsius
        self.atmosphere = atmosphere
        self.orbit = orbit


    def resume(self):
        base_resume = super().resume()
        planet_resume = f"{base_resume} | AVG_temp = {self.avg_temp_celsius}"
        if self.atmosphere is not None:
            planet_resume += f' | Atmosphere Composition: {self.atmosphere.composition_fraction}'
        if self.orbit is not None:
            planet_resume += f' | Orbit: {self.orbit}'
        return planet_resume