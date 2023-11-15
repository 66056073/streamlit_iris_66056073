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