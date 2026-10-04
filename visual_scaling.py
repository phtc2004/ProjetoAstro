from solar_system import *
import math


def visual_scale(celestial_body):
    if isinstance(celestial_body, Star):
        sun_visual_scale = 4
        ratio = celestial_body.radius_km / sun_object.radius_km
        scale = sun_visual_scale * ratio

    elif isinstance(celestial_body, Planet):
        earth_visual_scale = 0.5
        compression = 0.5
        ratio = celestial_body.radius_km / earth_object.radius_km
        scale = earth_visual_scale * (ratio**compression)

    elif isinstance(celestial_body, Moon):
        moon_visual_scale = 0.15
        ratio = celestial_body.radius_km / moon_object.radius_km
        scale = moon_visual_scale * ratio

    return scale


def visual_distance(celestial_body):
    if isinstance(celestial_body, Planet):
        ratio = celestial_body.orbit.distance_km / 57909227
        base_distance = 5
        spacing = 15
        scale = base_distance + spacing * math.log10(ratio)

    elif isinstance(celestial_body, Moon):
        moon_visual_distance = 1.2
        compression = 0.5

        ratio = celestial_body.orbit.distance_km / moon_object.orbit.distance_km
        scale = moon_visual_distance * (ratio ** compression)

    return scale


def visual_rotation_speed(celestial_body):

    earth_rotation_period = 23.9345
    earth_visual_rotation = 50.9
    ratio = earth_rotation_period / celestial_body.rotation_period_hours
    scale = earth_visual_rotation * ratio

    return scale


def visual_orbit_speed(celestial_body):

    earth_orbital_period = 365.256
    earth_visual_orbit_speed = 0.5
    ratio = earth_orbital_period / celestial_body.orbit.orbital_period_days
    scale = earth_visual_orbit_speed * ratio

    return scale
