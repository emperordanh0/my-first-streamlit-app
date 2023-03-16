import pickle
import streamlit as st
import numpy as np

model = pickle.load(open('model.pickle', "rb"))
x = np.array(st.number_input('Input Temperature'))
x = x.reshape(-1,1)
if st.button('Predict'):
  y = model.predict(x)
  st.success(y)
