import folium


map = folium.Map(location=[38.58, -99.09],zoom_start=6, tiles="Mapbox Bright")

map.add_child(folium.Marker(location=[38.1, -99.1], popup="I am a popup", icon=folium.Icon(color='red')))


map.save("Map1.html")
