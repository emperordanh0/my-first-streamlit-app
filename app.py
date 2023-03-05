from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
import streamlit as st

st.title('Giải phương trình bậc nhất')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
    if a == 0:
        st.success('Phương trình có vô số nghiệm')
    else:
        st.success('Phương trình có 1 nghiệm ' + str(-b/a))