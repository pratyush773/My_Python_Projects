import folium
import pandas as pd

def color_getter(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev <3000:
        return 'orange'
    else :
        return 'red'


map = folium.Map(location=[38.58, -99.09],zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

data = pd.read_csv("Volcanoes.csv")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

for lt,ln,el in zip(lat, lon, elev) :
    #fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color=color_getter(el))))
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el)+"m", fill_color=color_getter(el), color='grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=(open('world2.json', 'r', encoding='utf-8-sig').read()),
style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg)
map.save("Map5.html")
