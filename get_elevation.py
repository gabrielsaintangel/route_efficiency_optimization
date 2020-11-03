import gpxpy
import gpxpy.gpx
from math import sin, cos, sqrt, atan2, radians
import time
#Constants
earth_radius_m = 6373.0 * 1000 #approx radius of the earth




def get_distance_two_points(lat1,lon1,lat2,lon2):
    lat1 = radians(lat1) #convert cartesian coordinates to radians
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1 #get distance between the two lat lon points
    dlat = lat2 - lat1

    #haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #get distance in meters
    distance = earth_radius_m * c
    return distance

if __name__ == "__main__":
    #parsing an existing route file#
    #open gpx file
    gpx_file = open('ASC2020 route.gpx')

    #pass file into gpxpy
    gpx = gpxpy.parse(gpx_file)

    prev_lat, prev_lon, current_lat, current_lon = 0,0,0,0
    prev_elevation, current_elevation = 0,0
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                current_lat = float(point.latitude)
                current_lon = float(point.longitude)
                current_elevation = float(point.elevation)
                print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))
                
                if prev_lat != 0:
                    print("distance between current and previous: " + str(get_distance_two_points(prev_lat,prev_lon,current_lat,current_lon)) + " m")
                if prev_elevation != 0:
                    print("difference in elevation between the two points: " + str(current_elevation - prev_elevation) + "\n\n")
                time.sleep(1)
                prev_lat = current_lat
                prev_lon = current_lon
                prev_elevation = current_elevation