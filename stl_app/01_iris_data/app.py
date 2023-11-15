import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Iris Species')
st.markdown('`Scatter plot` show **Iris Species**')

choices = ['sepal.length',
           'sepal.width',
           'petal.length',
           'petal.width']

selected_x_var = st.selectbox('Select parameter for X axis', choices)
selected_y_var = st.selectbox('Select parameter for Y axis', choices)

iris_file = st.file_uploader('Select Iris file csv and upload', type=['csv'])

if iris_file is not None:
    iris_df = pd.read_csv(iris_file)
else:
    st.stop()

