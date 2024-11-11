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
st.image(image, use_column_width=True)

# Thanks to Igor Bumba for the image. Attribution below
# Photo by <a href="https://unsplash.com/@igorbumba?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"> Igor Bumba
# </a> on <a href="https://unsplash.com/photos/black-mercedes-benz-convertible-car-parked-on-grass-field-UIk-rF4Df60?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">
# Unsplash</a>

# Page Description
st.write("""
# VEHICLE SALES IN THE U.S.
This page shows the statistics of vehicle sales in the U.S. base on different variables.
***        
""")

####################
# PAGE BODY
####################

# Load dataset
vehicles = pd.read_csv('vehicles_us.csv')

st.header('View Dataset')
# Add a 'manufaturer' column in the dataset for easier reference
vehicles['manufacturer'] = vehicles['model'].apply(lambda x: x.split()[0])
st.dataframe(vehicles)
st.write("""       
""")

st.header('Vehicle Condition Per Manufacturer')
# Plot the distribution of vehicle's condition by the manufacturer
fig = px.histogram(vehicles, 
                   x="manufacturer", 
                   color="condition", 
                   height=600, 
                   width=1500)
fig.update_layout(xaxis={'categoryorder': 'category ascending'},
                 yaxis_title='Number of Vehicles Sold',
                 xaxis_title='Vehicle Manufacturer',
                 legend_title='Vehicle Condition')
st.write(fig)
st.write("""       
""")

