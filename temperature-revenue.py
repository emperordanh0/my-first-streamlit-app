import pickle
import streamlit as st
import matplotlib.pyplot as plt

model = pickle.load(open('model.pickle', "rb"))
if st.button('Go'):
  x_line = np.array([np.min(x), np.max(x)]).reshape(-1,1)
  y_line = model.predict(x_line)
  plt.scatter(x, y)
  plt.plot(x_line, y_line, color = 'red')
  plt.xlabel('Temperature')
  plt.ylabel('Revenue')
  plt.show()
