
import pandas as pd
from  sklearn.preprocessing import StandardScaler
data = {
    "car":['A','B','C','D','E','F','G'],
    "mpg" : [20,25,30,15,18,22,8],
    "horsepower" : [130,165,150,120,120,115,200],
    "weight" : [3500,3700,2800,3200,4000,3000,7000],
    "acceleration" : [12.0,11.5,14.0,13.0,10.5,15.0,9.0],
    "orgin":["USA","Europe","Japan","USA","Japan","Europe","USA"]
}

df = pd.DataFrame(data)
print("----------------------df----------------")
print(df)
print(df.columns)
print("----------------------------------------")
#standardization :
 # as we apply it only on numeric fileds selecting only this
numeric_colunms = ['horsepower','weight','acceleration']
df_std = df[numeric_colunms]
print(df_std)

scaler = StandardScaler()
x_std = scaler.fit_transform(df_std)
print("Original DF",df_std)
print("Standiztion :",x_std)

print("Mean is :", scaler.mean_)
print("Standard Deviation  :",scaler.var_)

