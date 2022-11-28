import streamlit as st
import altair as alt
import numpy as np  
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


st.title('Skill usage vs degree')
st.write("This is a chart I used for the midterm assignment, now made in python and using streamlit")
# load data
df = pd.read_csv("midterm cleaned.csv")
#st.write("EDA")
#st.write(df.describe().T)
#st.write(df.nunique())



##degree
##title
#seniority

        


#y = df["Avg Salary(K)"]

#x = df["Degree"]

#regr = linear_model.LinearRegression()
##regr.fit(x, y)

#st.bar_chart(df)



#td =plt.bar(x=df['Degree'],height=df['Avg Salary(K)'])

#td = pd.DataFrame(df["Degree"],df["Avg Salary(K)"]).T

#st.pyplot(td)

#val_count  = df['Python'].value_counts()

#df1 = df['Degree'].value_counts().rename_axis('unique_values').reset_index(name='counts')


#st.bar_chart(df1)


option = st.selectbox(
    'What skills each degree uses:',
    ('Python', 'spark', 'aws',"excel","sql","sas","tensor"))

st.write('You selected:', option)

#option='aws:Q'



bar_chart = alt.Chart(df).mark_bar().encode(
        y=option,
        x='Degree:O',
    )
 
st.altair_chart(bar_chart, use_container_width=True)



