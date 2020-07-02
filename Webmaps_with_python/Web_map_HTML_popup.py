import folium
import pandas as pd


data = pd.read_csv("Volcanoes.csv")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])


html = """<h4>Volcano information:</h4>
Height: %s m
"""


map = folium.Map(location=[38.58, -99.09],zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")


#for lt,ln,el in zip(lat, lon, elev) :
#    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+"m", icon=folium.Icon(color='red')))

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))

map.add_child(fg)
map.save("Map_html_popup_simple.html")
