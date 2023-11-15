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

st.subheader('Simple Data')
st.write(iris_df)

st.subheader('Scatter Plot')
sns.set_style('darkgrid')
markers = {"Setosa": "v", "Versicolor": "s", "Virginica": "o"}

fig, ax = plt.subplots()
ax = sns.scatterplot(data=iris_df,
                     x=selected_x_var, y=selected_y_var,
                     hue='variety', markers=markers, style='variety')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title('Iris Species Data')
st.pyplot(fig)



