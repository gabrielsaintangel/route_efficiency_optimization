import gpxpy
import gpxpy.gpx
import time
import plotly.express as px
import requests
from math import sin, cos, sqrt, atan2, radians, asin
from time import sleep

WEATHER_API_KEY = "ae9236e9ca6ea3794bdba089409750dc"

EARTH_RADIUS_M = 6373.0 * 1000 #approx radius of the earth

home = [42.294869, -89.00968]
school = [40.512048, -88.993168]


def get_distance_two_points(prev_point, curr_point) -> float:
    lon1, lat1, lon2, lat2 = map(radians, [prev_point.longitude, prev_point.latitude, curr_point.longitude,curr_point.latitude])


    # haversine formula 
 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r



def get_weather(points):
    weather = [] 
    for point in points:
        response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat" + 
                        point.latitude + "&lon=" + point.longitude + "&appid=" + WEATHER_API_KEY)
        weather.append(response)

def generate_graphs(points, distances, weather):
    elevations = [point.elevation for point in points]

    
    
    






if __name__ == "__main__":
    gpx_file = open('ASC2020 route.gpx')#open gpx file
    parsed_map = gpxpy.parse(gpx_file) #pass file into gpxpy

    points = []
    distances = []
    curr_distance = 0

    prev_point = None
    for track in parsed_map.tracks:
        for segment in track.segments:
            for curr_point in segment.points:
                if prev_point == None: # this is for the first iteration
                    prev_point = curr_point

                
                points.append(curr_point)
                distances.append(curr_distance)
                curr_distance += get_distance_two_points(curr_point, prev_point)
    
    # lets shorten the lists to every 50th element in order to expedite pulling weather data
    points = points[0::200]
    distances = distances[0::200]
    print(distances[5])

    print(len(points))


     
