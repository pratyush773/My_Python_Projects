import folium
import pandas as pd


map = folium.Map(location=[38.58, -99.09],zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")

data = pd.read_csv("Volcanoes.csv")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

for lt,ln,el in zip(lat, lon, elev) :
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map2.html")
