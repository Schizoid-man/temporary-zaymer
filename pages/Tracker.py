##
from streamlit_geolocation import streamlit_geolocation
import streamlit as st
from shapely.geometry import Point, Polygon
import geopandas as gpd
import pandas as pd
import geopy
from navigation import make_sidebar

make_sidebar()
location = streamlit_geolocation()
#st.write(location)


##

from geopy.geocoders import Nominatim

# initialize Nominatim API 
geolocator = Nominatim(user_agent="geoapiExercises")

# Latitude & Longitude input
Latitude = str(location['latitude'])
Longitude = str(location['longitude'])
try: 
 location2 = geolocator.reverse(Latitude+","+Longitude)
 # Display
 st.write("Detected near : " ,location2)
except:
 st.write("Click the location button to remove the error")
 



##
import folium
from streamlit_folium import st_folium
location3 = location['latitude'],location['longitude']
# center on Liberty Bell, add marker
m = folium.Map(location=location3, zoom_start=16)
folium.Marker(
    location3, popup=str(location3), tooltip=str(location3)
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
