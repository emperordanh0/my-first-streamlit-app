import streamlit as st
import plotly as plt
from sklearn.linear_model import LinearRegression

st.title('Giải phương trình bậc nhất')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
    if a == 0:
        st.success('Phương trình có vô số nghiệm')
    else:
        st.success('Phương trình có 1 nghiệm ' + str(-b/a))
