
from pandas.core.arrays import Categorical
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import  ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np


data = {
    "car":['A','B','C','D','E','F','G'],
    "mpg" : [20,25,30,15,18,22,8],
    "horsepower" : [130,165,150,120,120,np.nan,200],
    "weight" : [3500,3700,2800,3200,4000,3000,7000],
    "acceleration" : [12.0,11.5,14.0,13.0,10.5,np.nan,9.0],
    "orgin":["USA","Europe","Japan","USA","Japan","Europe","USA"]
}


df = pd.DataFrame(data)
print("----------------------df----------------")
print(df.columns)
print("----------------------------------------")
numeric_cols = ['horsepower','weight','acceleration']
categorical_cols = ['orgin']

numeric_transform = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='mean')),
        ('scaler',StandardScaler())
    ]
)

categorical_transform = Pipeline(
    steps=[
        ('imputer',SimpleImputer(strategy='most_frequent')),
        ('onehot',OneHotEncoder(handle_unknown='ignore'))
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ('num',numeric_transform,numeric_cols),
        ('cat',categorical_transform,categorical_cols)
    ]
)

x = df[numeric_cols + categorical_cols]
x_proccessed = preprocessor.fit_transform(x)
print(x_proccessed)
