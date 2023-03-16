import pickle
import streamlit as st
model = pickle.load(open(filename, "rb"))
if st.button('Go'):
