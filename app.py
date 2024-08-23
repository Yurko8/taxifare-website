import streamlit as st
import requests
import pandas as pd
import random


image_path = "images/istockphoto-177782877-612x612.jpg"
st.image(image_path, use_column_width=True)

'''
# New York Taxi Fare Predictor
'''

st.markdown('''
If you are ever thinking of getting a cab in New York?

If you do so and don't want to get scammed you need this website, as it allows you to accurately predict the fare prices!
''')

st.sidebar.header("Trip Details")

date = st.sidebar.date_input(label = "Please choose the date of the trip:", value = None)
time = st.sidebar.time_input(label = "Please choose the time of the trip:", value = None)
pickup_long = st.sidebar.number_input(label = "Please choose the pickup longitude:", value = random.uniform(-74.05, -73.75), placeholder = "Type in the number...")
pickup_lat = st.sidebar.number_input(label = "Please choose the pickup latitude:", value = random.uniform(40.63, 40.85), placeholder = "Type in the number...")
dropoff_long = st.sidebar.number_input(label = "Please choose the dropoff longitude:", value=random.uniform(-74.05, -73.75), placeholder = "Type in the number...")
dropoff_lat = st.sidebar.number_input(label = "Please choose the dropoff latitude:", value = random.uniform(40.63, 40.85), placeholder = "Type in the number...")
passenger_c = st.sidebar.slider(label = "How many passengers would that be?", min_value =1, max_value=8, step=1)

url_pred = "https://taxifare.lewagon.ai/predict"
params = {"pickup_datetime": f"{date} {time}",
          "pickup_longitude": pickup_long,
          "pickup_latitude": pickup_lat,
          "dropoff_longitude": dropoff_long,
          "dropoff_latitude": dropoff_lat,
          "passenger_count": passenger_c}

click = st.button(label="Get fare!")

data = pd.DataFrame({
    'lat': [pickup_lat, dropoff_lat],
    'lon': [pickup_long, dropoff_long]
})

st.map(data, size=20, color='#0044ff')

if click:
    fare_pred = requests.get(url = url_pred, params=params).json()
    st.write(f"Your predicted fare {round(fare_pred['fare'], ndigits=2)} Dollars!")
