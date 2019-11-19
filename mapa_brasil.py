import pandas as pd
import matplotlib.pyplot as plt

import geopandas as gpd
from shapely.geometry import Point


if __name__ == '__main__':

	shapefile = gpd.read_file("GeoData/BRMUE250GC_SIR.shp")
	df = pd.read_table("Dados/geo_municipios.csv", sep = ',')



	fig, ax = plt.subplots(figsize=(20, 20))
	shapefile.to_crs({"init": "epsg:4326"}).plot(ax=ax, color="white",
												 edgecolor="black")

	x = df['Lng']
	y = df['Lat']

	geometry = [Point(xy) for xy in zip(x, y)]        
	geo_df = gpd.GeoDataFrame(df, geometry=geometry)

	plt.scatter(x, y, alpha=0.5) #label = description[index])

	plt.legend()
