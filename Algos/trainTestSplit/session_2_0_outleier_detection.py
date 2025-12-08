
import pandas as pd
from sklearn.ensemble import IsolationForest
from  sklearn.preprocessing import OneHotEncoder
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

print("------------------ILoc----------------------")
encoder_colunms = ['horsepower','weight','acceleration']
encode_data = df[encoder_colunms]
print(encoder_colunms)
print("----------------------------------------")
#Normalization
isolation_model = IsolationForest(contamination=0.15,random_state=42)
labels = isolation_model.fit_predict(encode_data)
df['outlear_flag'] = labels
print(df.columns)
print(df) # so it will find as -1 for outlear so we can drop

