import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')

x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = [i+random.randint(-50,50) for i in x_axis ]

df = pd.DataFrame({'x': x_axis,'y': y_data})
st.write(df)

st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)



st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python'
)

scatter = alt.Chart(df).mark_point().encode(
    x='x',
    y='y',
    )
st.altair_chart(scatter, use_container_width=True)

st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("""
### The 5 changes I made were:

- **Change 1:** Added a title

- **Change 2:** Added a size variable (which grows the point depending on the variable used) which uses the a values(see code) but you can use a different column of data to visualize a 3rd variable in a 2d plane

- **Change 3:** Added a color variable (which shades the point depending on the variable used) uses the b values(see code) but you can use a different column of data to visualize a 4th variable in a 2d plane

- **Change 4:** Added a tooltip so you can highlight each point and see its characteristics

- **Change 5:** Adjusted size
""")

#######################remaking the dataset for more variables
x_limit = 100

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange(0,x_limit,1)

# Create a random array of data that we will use for our y values
y_data = [i+random.randint(-50,50) for i in x_axis ]
a_data = [i+random.randint(-50,50) for i in x_axis ]
b_data = [i+random.randint(-50,50) for i in x_axis ]
df = pd.DataFrame({'x': x_axis,'y': y_data,'a': a_data,'b': b_data})
######################################################################

scatter_4 = alt.Chart(df).mark_point().encode(
    x='x',
    y='y',
    size="a",
    color="b",
    tooltip=["x","y","a","b"],
    
    ).properties(width=400,
    height=600,
    title="This is a title!"
)
st.altair_chart(scatter_4, use_container_width=True)

"""
scatter2 = alt.Chart(df).mark_point().encode(
    x='x',
    y='y',
    tooltip=["x","y"],
    ).properties(
    title="Change 5 A regression line!"
)

scatter2=scatter2+scatter2.transform_regression('x', 'y').mark_line()
st.altair_chart(scatter2, use_container_width=True)
"""

st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets \n"
)
st.write("Before:")
from vega_datasets import data

source = data.iowa_electricity()
st.write(source)
base = alt.Chart(source).mark_area(opacity=0.3).encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack=None),
    color="source:N"
)
st.altair_chart(base, use_container_width=True)

st.markdown("""
The 2 changes I made were:
- Change 1: added a title and changed opacity
- Change 2: reconfigured size
"""
)

base = alt.Chart(source).mark_area(opacity=0.8).encode(
    x="year:T",
    y=alt.Y("net_generation:Q", stack=None),
    color="source:N"
).properties(
    title="This is a title",
    width=500,
    height=550
)
st.altair_chart(base, use_container_width=True)


