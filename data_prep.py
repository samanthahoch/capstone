import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon, shape

# data source: https://s3.amazonaws.com/hubway-data/index.html
blue_bikes_csv = pd.read_csv("data/201501-hubway-tripdata.csv")

start_points = [Point(xy) for xy in zip(blue_bikes_csv['start station longitude'], blue_bikes_csv['start station latitude'])]
start_df = gpd.GeoDataFrame(blue_bikes_csv, crs=4326, geometry=start_points)

end_points = [Point(xy) for xy in zip(blue_bikes_csv['start station longitude'], blue_bikes_csv['start station latitude'])]
points = zip(start_points, end_points)
data = {'type': 'MultiLineString', 'coordinates': points}
data_shape = shape(data)


end_df = gpd.GeoDataFrame(blue_bikes_csv, crs=4326, geometry=end_points)

fig, ax = plt.subplots(figsize=(7, 7))
start_df.plot(ax=ax, markersize=20, color="blue", marker="^", label="start")
start_df.plot(ax=ax, markersize=20, color="red", marker="^", label="end")
plt.show()