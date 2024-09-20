import streamlit as st
import requests
import pandas as pd

# Function to get location data based on IP address
def get_location():
    try:
        # Call to IPinfo API to get the geolocation based on the user's IP
        response = requests.get("https://ipinfo.io")
        data = response.json()
        
        # Extract latitude and longitude from the "loc" key
        loc = data.get("loc", None)
        if loc:
            lat, lon = map(float, loc.split(','))
            return lat, lon
        else:
            return None, None
    except Exception as e:
        st.error(f"Error retrieving location: {e}")
        return None, None

# Get user input as a string for age
t = st.text_input("Enter the age")

# Convert input to an integer if possible
if t:
    try:
        t = int(t)  # Convert to integer
        if t < 18:
            st.error("FBI open up!!!")
            st.camera_input("open the damn door")
            
            # Fetch the location only if the user is under 18
            latitude, longitude = get_location()

            # Check if we got a valid location and display the map
            if latitude and longitude:
                map_data = pd.DataFrame({'latitude': [latitude], 'longitude': [longitude]})
                st.map(map_data, use_container_width=True)
            else:
                st.write("Unable to fetch location from your IP address.")
        elif t >= 18:
            st.success("Good to go")
        print(t)
    except ValueError:
        st.error("Please enter a valid age")
