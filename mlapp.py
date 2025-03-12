import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Create a title for your app
st.title('Machine Learning Classification App')

## fn to load iris dataset
@st.cache_data
def load_data():
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df

df = load_data()

## Display the dataframe
st.write("Here's our first dataframe:")
st.write(df)


