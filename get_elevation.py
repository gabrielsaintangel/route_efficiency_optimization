import gpxpy
import gpxpy.gpx
from math import sin, cos, sqrt, atan2, radians
import time
import plotly.express as px
#Constants
earth_radius_m = 6373.0 #approx radius of the earth


def get_distance_two_points(prev_coordinates,current_coordinates):
    lat1 = radians(prev_coordinates[0]) #convert cartesian coordinates to radians
    lon1 = radians(prev_coordinates[1])
    lat2 = radians(current_coordinates[0])
    lon2 = radians(current_coordinates[1])

    dlon = lon2 - lon1 #get distance between the two lat lon points
    dlat = lat2 - lat1

    #haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #get distance in meters
    distance = earth_radius_m * c
    return distance


if __name__ == "__main__":
    gpx_file = open('ASC2020 route.gpx')#open gpx file
    gpx = gpxpy.parse(gpx_file) #pass file into gpxpy

    prev_coordinates, current_coordinates = [0,0],[0,0] #pairs of lat and lon coordinates
    prev_elevation, current_elevation = 0,0 #compare the difference in elevation over two coordinates
    starting_coordinates, ending_coordinates = [0,0],[0,0] #pairs of lat and lon coordinates for perfoming summaries
    current_distance = 0 #distance from the last starting point
    total_distance = 0 #total distance of the route
    elevation_difference = 0 #difference in elevation from the last starting point
    elevation_data = [] # for graphing elevation along route, y axis
    distance_data = [] # for graphing elevation along route, x axis

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if starting_coordinates == [0,0]: #get starting coordinates for 1000m section
                    starting_coordinates = [point.latitude, point.longitude]

                current_coordinates = [float(point.latitude), float(point.longitude)] #current coordinates for calculations
                current_elevation = float(point.elevation)
                elevation_data.append(current_elevation) #add dictionary key and value to elevation data\
                distance_data.append(total_distance)
                #print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))
                
                if prev_coordinates != [0,0]:
                    current_distance += get_distance_two_points(prev_coordinates,current_coordinates) #add the current distance to the total distance for the period
                if prev_elevation != 0:
                    elevation_difference += (current_elevation - prev_elevation)

                if current_distance > 1000: #if 1000m subsection has been reached, make a decision regarding acceleration during this period
                    ending_coordinates = current_coordinates
                    print("Period distance =" + str(current_distance) + "kilometers")
                    print("Period coordinates: " + str(starting_coordinates) + ", " + str(ending_coordinates))
                    print("Average elevation along period: " + str(elevation_difference))
                    if(elevation_difference > 0):
                        print("This period is on average uphil, gain speed beforehand\n\n")
                    else:
                        print("This period is on average downhill, coast\n\n")
                    starting_coordinates = [0,0]
                    current_distance = 0
                    elevation_difference = 0
                total_distance += current_distance
                    
                prev_coordinates = current_coordinates
                prev_elevation = current_elevation
    

#graph data
fig = px.line(x=distance_data, y=elevation_data, color=px.Constant("Elevation"),
             labels=dict(x="Distance from Start in KM", y="Elevation in M", color="Legend"))
fig.show()#show graph in browser