import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from vega_datasets import data


################################Data stuff##########################################
df = pd.read_csv("data/Cleaned_Salaries.csv")
#st.write(df)

selection = df.iloc[:, [2,20,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]]
cols=["index","Job Title","Avg Salary(k)","Python","Spark","AWS","Excel","SQL","SAS","keras","pytorch","scikitlearn","TensorFlow","Tableau","PowerBI","Flink","MongoDB","Google An"]


#st.write(selection)
st.header("Salaries in Data Science")
# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])
#st.write('You selected:', options)
st.write("Add your skill set and see where your salary is")

options = st.multiselect(
    'What tools do you know?',
    ["Python","Spark","AWS","Excel","SQL","SAS","keras","pytorch","scikitlearn","TensorFlow","Tableau","PowerBI","Flink","MongoDB","Google An"],
    ['Python'])




#Figure 1 Salary vs title  Avg Salary(K)

df2=df.loc[df["Job Title"].isin(options)]
#st.write(df2)
st.write("FIGURE 1: Average Salary")


#st.write(df2)
c1=alt.Chart(df2).mark_bar().encode(
    alt.X("Avg Salary(K)",  bin=alt.Bin(maxbins=25)),
    y='count()',
)

st.altair_chart(c1, use_container_width=True)

