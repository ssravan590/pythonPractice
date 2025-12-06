import pandas as pd
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
import numpy
from Algos.trainTestSplit.TrainTestSplitAlgo import x_train

df= pd.read_csv("diabetes.csv")
print("-------------")
print("head of Data Frame :")
print(df.head())
print("Extracting Features ")
#x_data = df.iloc[:,:-1].values #all the values except the last row
#y_data = df.iloc[:,-1] #only the last one
#print("Type of  : ",type(x_data))
print("------above or below anything will work but above one is have more performance--")
x_data_feature = df.drop("Outcome",axis=1)
y_data_target = df['Outcome']
x_data = x_data_feature.values
y_data = y_data_target.values

kfold = KFold(n_splits=5)
scrores_test = []
for train_index,test_index in kfold.split(x_data):
    x_train,x_test = x_data[train_index],x_data[test_index]
    y_train,y_test = y_data[train_index],y_data[test_index]

    descion_tree = DecisionTreeClassifier(max_depth=2)

    descion_tree.fit(x_train,y_train)
    scrores_test.append(descion_tree.score(x_test,y_test))
print("average score :",scrores_test )
print("Mean if score :",numpy.mean(scrores_test))