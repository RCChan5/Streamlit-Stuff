import streamlit as st

import pandas as pd
import plotly.express as px
import altair as alt

st.set_page_config(layout = "wide")
df = pd.DataFrame(px.data.gapminder())
st.header("National Statistics")



st.write(df)
df["year"] = pd.to_datetime(df["year"],format="%Y").dt.year




st.write(df)