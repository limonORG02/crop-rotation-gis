import matplotlib.pyplot as plt
import geopandas as gpd




def plot_fields(gdf, column='crop_type', title=None, figsize=(10, 7)):
ax = gdf.plot(column=column, legend=True, figsize=figsize, edgecolor='black')
if title:
ax.set_title(title)
ax.set_axis_off()
return ax
