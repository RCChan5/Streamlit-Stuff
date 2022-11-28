import streamlit as st
import pandas as pd
import numpy as np
import altair as alt



################################Data stuff##########################################
df = pd.read_csv("data/Cleaned_Salaries.csv")
job_title_option = df["Job Title"].unique()


############################SIDE BAR################################################
st.sidebar.success("Select a demo above.")

#list of job titles to use in new df  ##should i keep this as a single value or multi
option1 = st.sidebar.multiselect(
    'Figure1: What job are you interested in?',
    job_title_option,["Data Scientist"])

#testing




###################################MAIN PAGE######################################

st.header("Salaries in Data Science")
# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])
#st.write('You selected:', options)
st.write("Add your skill set and see where your salary is")



#Figure 1 Salary vs title  Avg Salary(K)

df2=df.loc[df["Job Title"].isin(option1)]
#st.write(df2)
st.write("FIGURE 1: Average Salary")


#st.write(df2)
c1=alt.Chart(df2).mark_bar().encode(
    alt.X("Avg Salary(K)",  bin=alt.Bin(maxbins=25)),
    y='count()',
)

st.altair_chart(c1, use_container_width=True)

## Figure 2

st.write("FIGURE 2: What type of Degrees are used in the field?")


#st.write(df2)
c2=alt.Chart(df2).mark_bar().encode(
    x="Degree",
    y='count()',
)

st.altair_chart(c2, use_container_width=True)

## Figure 3

st.write("FIGURE 3: Senority level")


#st.write(df2)
c3=alt.Chart(df2).mark_bar().encode(
    x="seniority_by_title",
    y='count()',
)

st.altair_chart(c3, use_container_width=True)








