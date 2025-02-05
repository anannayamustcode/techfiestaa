import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from pydantic import BaseModel


version ='__0.1.0__'

df= pd.read_excel(r'assets/final.xlsx')


scaler = StandardScaler(copy=False)

X=df[['Lat', 'Lon']]
Y=df['Crm Score']

knn = KNeighborsRegressor(n_neighbors=5)

X_scaled=scaler.fit_transform(X)

knn.fit(X_scaled, Y)


def predict_score(lat, lon):
    loc = scaler.transform([[lat, lon]])
    score=knn.predict(loc)
    return score




