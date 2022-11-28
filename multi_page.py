import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt


st.set_page_config(layout = "wide")
df = pd.DataFrame(px.data.gapminder())
st.header("National Statistics")
st.write("jsahdks")



page = st.sidebar.selectbox('Select page',
  ['Country data','Continent data'])


if page == "Country data":
    clist = df["country"].unique()
    country = st.selectbox("select a country",clist)

    col1,col2 = st.columns(2)
    sd_country = df[df["country"]== country]
    GDP_Chart = alt.Chart(sd_country).mark_line().encode(
        x = "year",
        y = "gdpPercap"
        )

    col1.altair_chart(GDP_Chart, use_container_width=True)
    GDP_pop = alt.Chart(sd_country).mark_line().encode(
        x = "year",
        y = "pop"
        )
    col2.altair_chart(GDP_pop, use_container_width=True)

else:
    contlist = df["continent"].unique()

    continent = st.selectbox("Select a continent:",contlist)

    col1,col2 = st.columns(2)

    df = df[df['continent'] == continent]

    fig = px.line(df[df['continent'] == continent], 
    x = "year", y = "gdpPercap",
    title = "GDP per Capita",color = 'country')

    col1.plotly_chart(fig)

    fig = px.line(df[df['continent'] == continent], 
    x = "year", y = "pop",
    title = "Population",color = 'country')

    col2.plotly_chart(fig, use_container_width = True)