import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np



df_vehicles= pd.read_csv('vehicles_us.csv')


st.header('Used Car Data')

st.write('Use the Data to learn about used cars and their value')

#changed to datetime datatype
df_vehicles['date_posted'] = pd.to_datetime(df_vehicles['date_posted'])

# I filled in the missing columns with the median of each.
df_vehicles[['model_year','cylinders','odometer']] = df_vehicles.groupby('model')[['model_year','cylinders','odometer']].transform(lambda x: x.fillna(x.median()))

#Some of the missing values did not get removed from the above code.
#df_vehicles = df_vehicles.dropna(subset=['odometer'])

#adding median to the missing 41 values.
df_vehicles['odometer'] = df_vehicles['odometer'].fillna(df_vehicles['odometer'].median())

#I filled in missing values with zeros. 
df_vehicles['is_4wd'] = df_vehicles['is_4wd'].fillna(0)



#changed columns values of float to int
df_vehicles[['model_year','cylinders','odometer','is_4wd']] = df_vehicles[['model_year','cylinders','odometer','is_4wd']].astype(int)

#convert is_4wd to boolean
df_vehicles['is_4wd'] = df_vehicles['is_4wd'].astype(bool)

df_vehicles['price'] = pd.to_numeric(df_vehicles['price'], errors = 'coerce')

#filled missing paint color with the mode white
#mode_paint_color = df_vehicles['paint_color'].mode()[0]
df_vehicles['paint_color'] = df_vehicles['paint_color'].fillna('unknown')

#make a new column with brand namestream
df_vehicles['brand'] = df_vehicles['model'].str.split().str.get(0)

brands = df_vehicles['brand'].unique()
selected_brand = st.selectbox('Select a brand', brands)


min_odometer = df_vehicles['odometer'].min()
max_odometer = df_vehicles['odometer'].max()
odometer_range = st.slider("Choose Odometer Range", value =(min_odometer,max_odometer) , min_value = min_odometer, max_value = max_odometer)


st.write('Choose Cylinders')
six_cylinders = st.checkbox("6", value = True)
eight_cylinders = st.checkbox("8", value = True)


cylinders_select = []
if six_cylinders:
    cylinders_select.append(6)
if eight_cylinders:
    cylinders_select.append(8)


df_filtered = df_vehicles[
    (df_vehicles['brand'] == selected_brand) &
    (df_vehicles['odometer'] >= odometer_range[0]) &
    (df_vehicles['odometer'] <= odometer_range[1]) & (df_vehicles['cylinders'].isin(cylinders_select))
]

df_filtered



st.header('Visuals')


st.write('Distribution of Price depending on Brand, Cylinders, Paint color, and Type')

distribution = ['brand', 'cylinders','type', 'paint_color']

selection = st.selectbox('Price VS ' , distribution)

fig1 = px.histogram(df_vehicles, x = 'price' , color = selection)
fig1.update_layout(title = 'Price distribution' ,xaxis= dict(range=[0,50000]))
st.plotly_chart(fig1)



st.write('Scatter plot of price depending on model year and brad')
brand_year_mean_price = df_vehicles.groupby(['brand','model_year'])['price'].mean().reset_index()


fig2 = px.scatter(brand_year_mean_price, x ='model_year', y = 'price' , color = 'brand')
fig2.update_layout(title= ' Mean Price by Brand and Model Year')
st.plotly_chart(fig2)

