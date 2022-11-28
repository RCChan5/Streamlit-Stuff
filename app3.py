import pandas as pd
import plotly.express as px
import streamlit as st
import altair as alt
df=pd.DataFrame(px.data.gapminder())


st.write("helloworld")



option = st.selectbox(
    'year:',
    ('1980','1990',"1991"))

st.write('You selected:', option)

option2 = st.selectbox(
    'What skills each degree uses:',
    ("Egypt","Afghanistan"))

st.write('Your country selected:', option2)

df=df[df(option) & df(option2)]
st.write(df)



