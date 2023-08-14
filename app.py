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

num1  = st.number_input("select a number", min_value = 0)
num2  = st.number_input("select another number", min_value = 0)
num3  = st.number_input("select one more number", min_value = 0)
if (num1 > num2) and (num1 > num3):
        st.header('Result')
        st.subheader("The largest of the 3 numbers is num1 ")
elif (num2 > num1) and (num2 > num3):
        
        st.header('Result')
        st.subheader("The largest of the 3 numbers is num2 ")
else:
        
        st.header('Result')
        st.subheader("The largest of the 3 numbers is num3 ")

    

st.header('User Input Parameters')
st.subheader('User Input parameters')
st.subheader('Pre-processed Input to the Model')
st.subheader('Class labels and their corresponding index number')
st.subheader('Prediction')
st.subheader('Prediction Probability')
# st.write(prediction_proba)
