from celestial_body import CelestialBody

class Star(CelestialBody):

    def __init__(self, name, radius_km, mass_kg, gravity, rotation_period_hours, spectral_class, effective_temp_kelvin, composition_fraction, solar_luminosity):
        super().__init__(name, radius_km, mass_kg, gravity, rotation_period_hours)
        self.spectral_class = spectral_class  
        self.effective_temp_kelvin = effective_temp_kelvin        
        self.composition_fraction = composition_fraction  
        self.solar_luminosity = solar_luminosity 

    def resume(self):
        base_resume = super().resume()
        star_resume = (
            f"{base_resume}"
            f" | SC = {self.spectral_class}"
            f" | ETK = {self.effective_temp_kelvin}"
            f" | C = {self.composition_fraction}"
            f" | SL = {self.solar_luminosity}")        
        return star_resume
