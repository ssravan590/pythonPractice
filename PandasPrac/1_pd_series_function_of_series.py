import numpy
import pandas as pd
import  sys as sys
book = ['Python','Java','DS','C','Golang', numpy.nan]

s = pd.Series(book,index=[i*10 for i in range(6)])
print(s.values)
print(s.index)
print(s.is_unique)
print(s.is_monotonic_decreasing)
print(s.is_monotonic_increasing)
print(s.hasnans)
print(s.size)
print(s.shape)

num = [12,23,54,2,3,4,5,656,4,2323232,2324,566,32]

s = pd.Series(num)
print("Max :")
print(max(s))
print(f"min is {min(s)}")