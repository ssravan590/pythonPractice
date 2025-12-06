import pandas as pd
import sklearn.model_selection as model_train_test_split

df = pd.read_csv("diabetes.csv")
print(df.head())
shuffle_df = df.sample(frac=1)
print("after shuffle")
print(shuffle_df.head())
print(shuffle_df.info())

# divide the data to 30 test and 80 train
train_size = int(0.7 * len(df))
print(train_size)

train_set = shuffle_df[:train_size]
test_set = shuffle_df[train_size:]
print("----trainSet---------")
print(train_set)
print("----testSet----------")
print(test_set)
print(f"Size of Train Set {len(train_set)} and Test Set {len(test_set)}")
train_set.groupby(['Outcome'])
test_set.groupby(['Outcome'])
print(f"dropping outcome from train")
features = df.drop('Outcome',axis=1) # axis= 0 is row and axis =1 is coulmns
target = df['Outcome']

print(features)
print(target)

x_train,x_test,y_train,y_test = model_train_test_split.train_test_split(features,target,test_size=0.3)




