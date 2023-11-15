import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import pickle


iris_df = pd.read_csv('iris.csv')
iris_df.dropna(inplace=True)
output = iris_df['variety']
