import geopandas as gpd
import self as self

gdf = gpd.read_file("/Users/alexis/Downloads/ai data/pavements_uk.csv") #read initial file into geodataframe works with wkt csv or gpkg doesn't work with a shapefile
gdf.crs = 'epsg:27700'# you need a crs that is in meters and not degrees. For instance epsg:4326 is in degrees and will not work
print(gdf.head(),'File loaded')
dissolve = gdf.dissolve("featureCod")
print(dissolve.head(),'dissolve completed')
dissolve.to_file("/Users/alexis/Downloads/ai data/dissolve.gpkg", layer="dissolve", driver="GPKG") #write the file other so you can in the next two rows remove the unnecessary gdfs from memory 
del gdf
del dissolve
buffer=gpd.read_file("/Users/alexis/Downloads/ai data/dissolve.gpkg", layer="dissolve", driver="GPKG")# could be broken in two steps with an a write and a read but works.
buffer1=buffer.buffer(-1)
buffer2=buffer1.buffer(1)
buffer2.to_file("/Users/alexis/Downloads/ai data/brighton/buffer2.gpkg", layer="buffer2", driver="GPKG")#these are the pavements over 2 meters
