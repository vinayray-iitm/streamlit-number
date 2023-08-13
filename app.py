import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Credit Card Approval Prediction App

This app predicts the credit card approval probablity
""")
#Get Input

st.header('User Input Parameters')
st.subheader('User Input parameters')
st.subheader('Pre-processed Input to the Model')
st.subheader('Class labels and their corresponding index number')
st.subheader('Prediction')
st.subheader('Prediction Probability')
# st.write(prediction_proba)
