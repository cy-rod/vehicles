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

# Thanks to Igor Bumba for the image. Attribution below.
# Photo by <a href="https://unsplash.com/@igorbumba?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash"> Igor Bumba
# </a> on <a href="https://unsplash.com/photos/black-mercedes-benz-convertible-car-parked-on-grass-field-UIk-rF4Df60?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">
# Unsplash</a>

# Page Description
st.write("""
# USED VEHICLE SALES
This *interactive page* shows the statistics of used vehicles sales base on different variables. Move the cursor to any data point on any charts for more information.
***        
""")


####################
# PAGE BODY
####################


##### TABLE 1 #####

# Load dataset
vehicles = pd.read_csv('vehicles_us.csv')
# Add a 'manufacturer' column in the dataset for easier reference
vehicles['manufacturer'] = vehicles['model'].apply(lambda x: x.split()[0])

# Add header
st.header('View Dataset')

# Display dataframe on streamlit
st.dataframe(vehicles)

# Add extra space
st.write("""       
""")


##### HISTOGRAM 1 #####

# Add header and "Tick box" instruction
st.header('Vehicle Condition Per Manufacturer')
st.write("""Tick/Untick the boxes on the right to sort by vehicle condition. Double click to isolate.""")

# Plot the histogram distribution of vehicle's condition by the manufacturer
fig = px.histogram(vehicles, x="manufacturer", color="condition", height=600, 
                  category_orders={"condition": ["new", "like new", "excellent", "good", "fair", "salvage"]})

# Sort category alphabetically and change axes and legend names
fig.update_layout(xaxis={'categoryorder': 'category ascending'},
                 yaxis_title='Number of Vehicles Sold',
                 xaxis_title='Vehicle Manufacturer',
                 font_family='Arial',
                 font_size=16,
                 legend_title='Vehicle Condition',
                 legend_font_size=14,
                 legend_title_font_size=14)

# Display figure on streamlit
st.plotly_chart(fig)

# Add extra space
st.write("""       
""")


##### HISTOGRAM 2 #####

# Add header and "Tick box" instruction
st.header('Fuel Type Per Vehicle Type')
st.write("""Tick/Untick the boxes on the right to sort by fuel type. Double click to isolate.""")

# Plot the distribution of fuel type per vehicle type
fig = px.histogram(vehicles, x="type", color="fuel", height=600,
                  category_orders={"fuel": ["gas", "diesel", "electric", "hybrid", "other"]})

# Sort category alphabetically and change axes and legend names
fig.update_layout(xaxis={'categoryorder': 'category ascending'},
                 yaxis_title='Number of Vehicles Sold',
                 xaxis_title='Vehicle Type',
                 legend_title='Fuel Type',
                 font_family='Arial',
                 font_size=16,
                 legend_font_size=14,
                 legend_title_font_size=14)

# Display figure on streamlit
st.plotly_chart(fig)

# Add extra space
st.write("""       
""")


##### HISTOGRAM 3 #####

# Add header and "Tick box" instruction
st.header('Distribution of Vehicle Type Per Year Model')
st.write("""Tick/Untick the boxes on the right to sort by vehicle type. Double click to isolate.""")

# Make a sorted list of vehicle type
type_list = sorted(vehicles['type'].unique())

# Plot distribution of vehicle type by the year model
fig = px.histogram(vehicles, x="model_year", color="type", height=700,
                  category_orders={"type": type_list})

# Change axes and legend names
fig.update_layout(yaxis_title='Number of Vehicles Sold',
                 xaxis_title='Year Model',
                 legend_title='Vehicle Type',
                 font_family='Arial',
                 font_size=16,
                 legend_font_size=14,
                 legend_title_font_size=14)

# Display figure on streamlit
st.plotly_chart(fig)

# Add extra space
st.write("""       
""")


##### HISTOGRAM 4 #####

# Add header and "Tick box" instruction
st.header('Distribution of Manufacturer Per Year Model')
st.write("""Tick/Untick the dots on the right to sort by vehicle manufacturer. Double click to isolate.""")

# Make a sorted list of vehicle manufacturers
manufac_list = sorted(vehicles['manufacturer'].unique())

# Plot distribution between vehicle manufacturer and the year model
fig = px.scatter(vehicles, x='model_year', color='manufacturer', height=900,
                category_orders={"manufacturer": manufac_list})

# Change axes and legend names
fig.update_layout(yaxis_title='Vehicle Index',
                 xaxis_title='Year Model',
                 legend_title='Manufacturer',
                 font_family='Arial',
                 font_size=16,
                 legend_font_size=14,
                 legend_title_font_size=14)

# Display figure on streamlit
st.plotly_chart(fig)

# Add extra space
st.write("""       
""")


##### HISTOGRAM 5 #####

# Add header and "Tick box" instruction
st.header('Compare Price Distribution of Two Manufacturers Base on Vehicle Type')
st.write("""Tick/Untick the boxes on the right to sort by vehicle manufacturer. Double click to isolate.""")

# Create a box with dropdown menu for user to select vehicle type
# Use the sorted list of vehicle manufacturers and vehicle types above
type_sel = st.selectbox(label='Choose Vehicle Type',    # Title of the select box
                        options=type_list,              # Options listed in the select box
                        index=type_list.index('sedan')) # Default pre-selected option

# Create a box with dropdown menu for user to select first vehicle manufacturer
manufacturer_sel = st.selectbox(label='Compare (Select Manufacturer)',
                                options=manufac_list, 
                                index=manufac_list.index('toyota'))

# Create a box with dropdown menu for user to select second vehicle manufacturer
manufacturer_sel2 = st.selectbox(label='With (Select Manufacturer)',
                                options=manufac_list, 
                                index=manufac_list.index('honda'))

# Filter dataframe using boolean conditions and save it as a new dataframe 
boolean_cond = (vehicles['type'] == type_sel) & (vehicles['manufacturer'] == manufacturer_sel) | (vehicles['manufacturer'] == manufacturer_sel2)
vehicles_filtered = vehicles[boolean_cond]

# Create a histogram as the main (default) chart
fig = px.histogram(vehicles_filtered,
                    x='price',
                    nbins=30,
                    color='manufacturer',
                    opacity=0.8,
                    barmode='overlay',
                    height=600)

# Create histogram subplots base on vehicle condition
fig_facet = px.histogram(vehicles_filtered,
                    x='price',
                    nbins=30,
                    color='manufacturer',
                    opacity=0.8,
                    barmode='overlay',
                    facet_col='condition',
                    height=400)

# Change axes and legend name of the main plot
fig.update_layout(yaxis_title='Total Vehicle Sold',
                 xaxis_title='Vehicle Price (USD)',
                 legend_title='Manufacturer',
                 font_family='Arial',
                 font_size=16,
                 legend_font_size=14,
                 legend_title_font_size=14)

# Change axes and legend name of the subplots
fig_facet.update_layout(yaxis_title='Total Vehicle Sold',
                 legend_title='Manufacturer',
                 font_family='Arial',
                 font_size=16,
                 legend_font_size=14,
                 legend_title_font_size=14)

# Add a checkbox for user to separate plot by vehicle condition
sort = st.checkbox('Separate plots by vehicle condition')
if sort:
    st.plotly_chart(fig_facet)
else:
    st.plotly_chart(fig)

# Add extra space
st.write("""       
""")