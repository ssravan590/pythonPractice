
import pandas as pd
from  sklearn.preprocessing import LabelEncoder
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
print("----------------------------------------")
print("------------------ILoc----------------------")
cat_colunms = ['orgin']
cat_data = df['orgin']
print(cat_colunms)
print("----------------------------------------")
#Normalization
label_model = LabelEncoder()
label_fit = label_model.fit_transform(cat_data)
print("Label :",label_fit)

