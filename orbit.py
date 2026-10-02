class Orbit:

    def __init__(self, distance_km, orbital_period_days, orbital_speed_kms):
        self.distance_km = distance_km
        self.distance_au = self.distance_km / 149597870.7
        self.orbital_period_days = orbital_period_days
        self.orbital_speed_kms = orbital_speed_kms

    def __str__(self):
        return f"Distance KM = {self.distance_km} | OPD = {self.orbital_period_days} | OS Km/s = {self.orbital_speed_kms}"