import streamlit as st
import pandas as pd
import numpy as np

# Create a title for your app
st.title('My first Stream')

## Display a text
st.write('Hello Streamlit!')

## Create a dataframe

df = pd.DataFrame({
    'A': np.random.randn(10),
    'B': np.random.randn(10)
})

## Display the dataframe
st.write("Here's our first dataframe:")
st.write(df)

## Create a line chart

st.line_chart(df)


