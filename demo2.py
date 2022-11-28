import streamlit as st
import pandas as pd
import numpy as np

st.header("my first streamlit line chart")

chart_data= pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])

st.write(chart_data)
st.line_chart(chart_data)

st.header("how to use st . checkbox")
st.write("what would you like to order")
icecream = st.checkbox("icreame")
cofee = st.checkbox("cofee")
cola = st.checkbox("cola")

if icecream:
    st.write("nice here :icecream:")
if cofee:
    st.write("nice here :coffee:")
if cola:
    st.write("nice here :cup_with_straw:")
