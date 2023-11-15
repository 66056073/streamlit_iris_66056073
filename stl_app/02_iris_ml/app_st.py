import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title('Iris Classifier')
st.write('This app uses 4 inputs to predict the species of iris using'
         'a model built on the Iris dataset. Use the form below'
         ' to get started!')