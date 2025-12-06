import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

enos = [100,200,300,400]
enames = ['A','B','C','D']
esals = [10000.0,20000.0,30000.0,40000.0]
eaddres =['Bang','Hyd','Pune','Delhi']
s = pd.Series(enames)
print("-------series 1d ---------")
print(s)
print(s.ndim)
print(s.shape)
print("------- 1d ---------")
print("---------DataFrame----------")
df = pd.DataFrame({'enos':enos,'enames':enames,'esals':esals,'eaddres':eaddres})
print(df)
print(df.ndim)
print(df.shape)
print(df.enames)


