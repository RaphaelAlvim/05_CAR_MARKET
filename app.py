import pandas as pd
import plotly_express as px
import streamlit as st

car_data = pd.read_csv('C:\\Users\\Raphael\\Documents\\GitHub\\05_CAR_MARKET\\vehicles.csv')

st.header('Find your new car here!', divider='rainbow')
st.header('_The Best Makes_ in one click :blue[cool] :sunglasses:')

hist_button = st.button('Create a histogram')  # criar um botão

if hist_button:
    # se o botão for clicado
    # escrever uma mensagem
    st.write('Creating a histogram with price distribution')

    # criar um histograma
    fig = fig = px.histogram(car_data,
                             x="price",
                             title='Price Distribution',
                             color_discrete_sequence=['#f0bd6b'],
                             opacity=0.8)

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Create a Scatter Plot')  # criar um botão

if hist_button:
    # se o botão for clicado
    # escrever uma mensagem
    st.write('Creating a Scatter Plot with Vehicles Info')

    # criar um histograma
    fig = px.scatter(car_data,
                     x="odometer",
                     y="price",
                     color="model_year",
                     color_continuous_scale='Magma')

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
