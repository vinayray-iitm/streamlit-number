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

num1  = st.number_input("select a number num1", min_value = 0)
num2  = st.number_input("select another number num2", min_value = 0)
num3  = st.number_input("select one more number num3", min_value = 0)
if (num1 > num2) and (num1 > num3):
        st.header('Result')
        st.subheader("The largest of the 3 numbers is num1 ")
elif (num2 > num1) and (num2 > num3):
        
        st.header('Result')
        st.subheader("The largest of the 3 numbers is num2 ")
else:
        
        st.header('Result')
        st.subheader("The largest of the 3 numbers is num3 ")

    
