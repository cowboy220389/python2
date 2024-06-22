import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt

car_ad_df = pd.read_csv('https://practicum-content.s3.us-west-1.amazonaws.com/datasets/vehicles_us.csv')



st.set_page_config(layout = 'wide')

st.header('Data viewer')

st.dataframe(car_ad_df)

st.header('Price by Odometer') #to find how miles affect car depreciation

fig = px.scatter(car_ad_df, x='odometer', y ='price')
st.write(fig)

st.header('Price by Model Year') # to tell how much cars depreciate by year

fig = px.histogram(car_ad_df, x = 'model_year', y = 'price')
st.write(fig)

st.header('Compare Price by Model Year')
# Get a list of production years
model_year_list = sorted(car_ad_df['model_year'].unique())

model_year_chosen = st.selectbox( label='Choose a Model Year',
                                 options= model_year_list,
                                 index= model_year_list.index(2006)
                                )
                   
mask_filter = car_ad_df['model_year']==model_year_chosen

df_filtered = car_ad_df[mask_filter]

normalize = st.checkbox('Normalize Histogram', value= True)

if normalize:
    histnorm = 'percent'
else: 
    histnorm = None

fig = px.histogram(df_filtered,
                   x = 'model_year',
                   nbins=50,
                   y ='price',
                   histnorm=histnorm,
                   barmode='overlay'
                    )
st.write(fig)