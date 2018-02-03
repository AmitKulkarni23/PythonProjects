import folium

"""
Note folium converts the map into a HTML and Javascript
"""

# The file name where the map will be save
map_name = "Map1.html"

# List which has the latitude and the longitude
lat_long_list = [38.58, -99.09]

# The initial zoom parameter
zoom_level = 6

# The name of the feature group parameter
feature_group_name = "My map"

# The color of the markers
marker_color = "green"

# The popup string
popup_string = "MARKER"

# Creating Map Object
map = folium.Map(location=lat_long_list, zoom_start=zoom_level, tiles="Mapbox Bright")

# Adding marker to the map object
# map.add_child(folium.Marker(location=lat_long_list, popup="Kansas"))


# Instead of adding a marker directly, create a feature group first
# Multiple features can be added to a feature group
fg = folium.FeatureGroup(name=feature_group_name)
fg.add_child(folium.Marker(location=lat_long_list, popup=popup_string, icon=folium.Icon(color=marker_color)))


# Adding data from a json file
# Creating the GeoJson object
# This is used to display the polygons on the map


fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read()))

# Adding the feature group to the map
map.add_child(fg)

# layer Control can be added to turn on features based on user choice
# A layer control menu is displayed on the HTMl page
# The user can choose to display or hide a layer


# This command gives the user only 1 option to the user
# turn all the features on or off.(because we have only 1 feature group)

map.add_child(folium.LayerControl())

# Saving the map
map.save(map_name)
