import pandas as pa
import pandas as pd
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

s = pa.Series([i for i in range(20)])
l = [3,4,5]
print(s[l])  # able to fetch values using list of indeces

alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print(alpha)

s1 = pd.Series(alpha)
print(s1[:])
print("i am using slice in series")
print(s1[2:8:2])
print(s1[s1.size-1])