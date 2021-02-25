import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon

# data source: https://s3.amazonaws.com/hubway-data/index.html
blue_bikes_csv = pd.read_csv("data/201501-hubway-tripdata.csv")

geometry = [Point(xy) for xy in zip(blue_bikes_csv['start station longitude'], blue_bikes_csv['start station latitude'])]
geo_df = gpd.GeoDataFrame(blue_bikes_csv, crs=4326, geometry=geometry)
geo_df.head()

fig, ax = plt.subplots(figsize=(15, 15))
geo_df.plot(ax=ax, markersize=20, color="blue", marker="^", label="start")