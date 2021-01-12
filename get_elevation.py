import gpxpy
import gpxpy.gpx
from math import sin, cos, sqrt, atan2, radians
import time
import plotly.express as px
#Constants
EARTH_RADIUS_KM = 6373.0 #approx radius of the earth


def get_distance_two_points(prev_coordinates,current_coordinates) -> float:
    lat1 = radians(prev_coordinates.latitude) #convert cartesian coordinates to radians
    lon1 = radians(prev_coordinates.longitude)
    lat2 = radians(current_coordinates.latitude)
    lon2 = radians(current_coordinates.longitude)

    dlon = lon2 - lon1 #get distance between the two lat lon points
    dlat = lat2 - lat1

    #haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #get distance in meters
    distance = EARTH_RADIUS_KM * c
    return distance


# We dont need every point from the map, this would create time constrains when making API requests
# Using the get_distance_two_points() function, lets get cooordinates for every 1000 meter period
def get_periodic_points(parsed_map) -> list:
    periodic_points = []
    prev_point = 0
    for track in parsed_map.tracks:
        for segment in track.segments:
            for point in segment.points:

                
    p
    print(total)
    

gpx_file = open('ASC2020 route.gpx')#open gpx file
parsed_map = gpxpy.parse(gpx_file) #pass file into gpxpy
make_elevation_graph(parsed_map)