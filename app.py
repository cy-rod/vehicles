# -*- coding: utf-8 -*-
# Import Libraries
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

####################
# PAGE TITLE
####################

# Load photo to the page
image = Image.open('vintage_car.png')
st.image(image, use_container_width=True)

# Thanks to Igor Bumba for the image. Attribution below
# Photo by <a href="https://unsplash.com/@igorbumba?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"> Igor Bumba
# </a> on <a href="https://unsplash.com/photos/black-mercedes-benz-convertible-car-parked-on-grass-field-UIk-rF4Df60?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">
# Unsplash</a>

# Page Description
st.write("""
# VEHICLE SALES IN THE U.S.
This *interactive page* shows the statistics of vehicle sales in the U.S. base on different variables. Move the cursor to any data point for more information.
***        
""")

####################
# PAGE BODY
####################

# Load dataset
vehicles = pd.read_csv('vehicles_us.csv')

# Add header
st.header('View Dataset')
# Add a 'manufacturer' column in the dataset for easier reference
vehicles['manufacturer'] = vehicles['model'].apply(lambda x: x.split()[0])
# Display dataframe on streamlit
st.dataframe(vehicles)
# Add extra space
st.write("""       
""")

# Add header and "Tick box" instruction
st.header('Vehicle Condition Per Manufacturer')
st.write("""Tick/Untick the boxes on the right to sort by condition. Double click to isolate.""")
# Plot the histogram distribution of vehicle's condition by the manufacturer
fig = px.histogram(vehicles, x="manufacturer", color="condition", height=600)
# Sort category alphabetically and change axes and legend names
fig.update_layout(xaxis={'categoryorder': 'category ascending'},
                 yaxis_title='Number of Vehicles Sold',
                 xaxis_title='Vehicle Manufacturer',
                 legend_title='Vehicle Condition')
# Display figure on streamlit
st.plotly_chart(fig)
# Add extra space
st.write("""       
""")

# Add header and "Tick box" instruction
st.header('Fuel Type Per Vehicle Type')
st.write("""Tick/Untick the boxes on the right to sort by fuel type. Double click to isolate.""")
# Plot the distribution of fuel type per vehicle type
fig = px.histogram(vehicles, x="type", color="fuel", height=600)
# Sort category alphabetically and change axes and legend names
fig.update_layout(xaxis={'categoryorder': 'category ascending'},
                 yaxis_title='Number of Vehicles Sold',
                 xaxis_title='Vehicle Type',
                 legend_title='Fuel Type')
# Display figure on streamlit
st.plotly_chart(fig)
# Add extra space
st.write("""       
""")

# Add header and "Tick box" instruction
st.header('Distribution of Vehicle Type Per Year Model')
st.write("""Tick/Untick the boxes on the right to sort by vehicle type. Double click to isolate.""")
# Plot distribution of vehicle type by the year model
fig = px.histogram(vehicles, x="model_year", color="type", height=600)
# Change axes and legend names
fig.update_layout(yaxis_title='Number of Vehicles Sold',
                 xaxis_title='Year Model',
                 legend_title='Vehicle Type')
# Display figure on streamlit
st.plotly_chart(fig)
# Add extra space
st.write("""       
""")

# Add header and "Tick box" instruction
st.header('Distribution of Manufacturer Per Year Model')
st.write("""Tick/Untick the dots on the right to sort by manufacturer. Double click to isolate.""")
# Plot distribution between vehicle manufacturer and the year model
fig = px.scatter(vehicles, x='model_year', color='manufacturer', height=700)
# Change axes and legend names
fig.update_layout(yaxis_title='Vehicle Index',
                 xaxis_title='Year Model',
                 legend_title='Manufacturer')
# Display figure on streamlit
st.plotly_chart(fig)
# Add extra space
st.write("""       
""")
