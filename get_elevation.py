import gpxpy
import gpxpy.gpx
import time
import plotly.express as px
import openweather as weather

#Constants

def generate_graphs(periodic_points):
    elevation_data = [point.elevation for point in periodic_points]
    






if __name__ == "__main__":
    gpx_file = open('ASC2020 route.gpx')#open gpx file
    parsed_map = gpxpy.parse(gpx_file) #pass file into gpxpy

    points = []
    for track in parsed_map.tracks:
        for segment in track.segments:
            for point in segment.points:
                points.append(point)

    periodic_points = points[0::20] # get every 20th point
    generate_graphs(periodic_points)
