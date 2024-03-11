import math
from api.client.client_main.models import Order


def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # Radius of the Earth in kilometers

    return distance


def filter_nearby_locations_order(user_latitude, user_longitude):
    nearby_locations = []
    for location in Order.objects.all():
        print(location)
        distance = calculate_distance(user_latitude, user_longitude, location.latitude, location.longitude)
        if distance <= 100:
            nearby_locations.append(location)

    return nearby_locations
