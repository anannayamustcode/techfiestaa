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
print(df.head())

scaler = StandardScaler()

X=df[['Lon', 'Lat']]
Y=df['Crm Score']

knn = KNeighborsRegressor(n_neighbors=5, algorithm='auto')

X_scaled=scaler.fit_transform(X)

knn.fit(X_scaled, Y)


def predict_score(lon, lat):
    loc = scaler.transform([[lon, lat]])
    score=knn.predict(loc)
    return score

df0=df[df.Clusters==0]
df1=df[df.Clusters==1]
df2=df[df.Clusters==2]
df3=df[df.Clusters==3]
df4=df[df.Clusters==4]

def show_on_map(lon, lat): 
    plt.figure(figsize=(100,80))
    plt.scatter(df0.Lon,df0.Lat, c='green')
    plt.scatter(df1.Lon,df1.Lat, c='orange')
    plt.scatter(df2.Lon,df2.Lat, c='grey')
    plt.scatter(df3.Lon,df3.Lat, c='purple')
    plt.scatter(df4.Lon,df4.Lat, c='brown')
    plt.plot(lon, lat, markerfacecolor='black', markersize=50, markeredgecolor='k', marker='o')
    plt.show()


