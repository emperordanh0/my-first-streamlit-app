import pickle
import streamlit as st

model = pickle.load(open('model.pickle', "rb"))
x = st.number_input('Input Temperature')
if st.button('Predict'):
  st.success(model.predict(x))
