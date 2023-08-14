import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Number Comparator

This app will compare two given  numbers
""")
#Get Input

value1  = st.number_input("select a number", min_value = 0)
value2  = st.number_input("select another number", min_value = 0)
value3  = st.number_input("select one more number", min_value = 0)

if value1 > value2:
    st.write("value1 is greater")
else:
    st.write("value2 is greater")

st.header('User Input Parameters')
st.subheader('User Input parameters')
st.subheader('Pre-processed Input to the Model')
st.subheader('Class labels and their corresponding index number')
st.subheader('Prediction')
st.subheader('Prediction Probability')
# st.write(prediction_proba)
