from math import sin, cos, sqrt, atan2, radians

def geo_distance(lat1, lon1, lat2, lon2):
    ''' haversine distance between two latitude longitude geo location '''

    # approximate radius of earth in m
    R = 6373.0 * 1000


    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance
