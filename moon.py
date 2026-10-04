from celestial_body import CelestialBody

class Moon(CelestialBody):

    def __init__(self, name, radius_km, mass_kg, gravity, rotation_period_hours, axial_tilt_degrees, orbit=None):
        super().__init__(name, radius_km, mass_kg, gravity, rotation_period_hours, axial_tilt_degrees)
        self.orbit = orbit

    def resume(self):
        base_resume = super().resume()
        moon_resume = f"{base_resume}"
        if self.orbit is not None:
            moon_resume += f' | {self.orbit}'
        return moon_resume

