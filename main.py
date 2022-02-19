import geopandas as gpd
import self as self

gdf = gpd.read_file("/Users/alexis/Downloads/ai data/pavements_uk.csv")
gdf.crs = 'epsg:27700'
print(gdf.head(),'Hi')
dissolve = gdf.dissolve("featureCod")
print(dissolve.head())

#buffer1=gdf.buffer(-1)
dissolve.to_file("/Users/alexis/Downloads/ai data/dissolve.gpkg", layer="dissolve", driver="GPKG")
del gdf
del dissolve
buffer=gpd.read_file("/Users/alexis/Downloads/ai data/dissolve.gpkg", layer="dissolve", driver="GPKG")
buffer1=buffer.buffer(-1)
buffer2=buffer1.buffer(1)
buffer2.to_file("/Users/alexis/Downloads/ai data/brighton/buffer2.gpkg", layer="buffer2", driver="GPKG")