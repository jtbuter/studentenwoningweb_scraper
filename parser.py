import cacher
import geopy.distance
import numpy

def get_houses():
    flatten = lambda l: [item for sublist in l for item in sublist]

    return flatten(cacher.cache())

def get_distance(a, b):
    return geopy.distance.geodesic(a, b).km

def results_in_radius(radius):
    scp = (52.3560, 4.9530)

    results = []

    for house in get_houses():
        sww = house["Latitude"], house["Longitude"]

        if get_distance(scp, sww) <= radius:
            results.append(house)

    return results
