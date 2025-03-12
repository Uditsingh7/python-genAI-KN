import streamlit as st
import pandas as pd
# title

st.title('Widgets')

## take user input
name = st.text_input('Enter your name:')

if name:
    st.write('Hello', name)
    
## take slider for age

age = st.slider('Enter your age:', 0, 100)

st.write('Your age is:', age)


## list options

options = st.multiselect('What are your favorite colors?',
                         ['Red', 'Green', 'Blue', 'Yellow', 'Orange'])

st.write('You selected:', options)


## upload a csv file

upload_file = st.file_uploader('Upload a CSV file:', type='csv')

if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.write(data)
    
    

