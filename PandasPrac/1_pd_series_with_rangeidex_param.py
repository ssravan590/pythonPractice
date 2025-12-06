
import pandas as pd
from setuptools.extern import names

book = ['Python','Java','DS']

s = pd.Series(data=book)
s.index = pd.RangeIndex(start=10,stop=13,step=1)
print(s)
print("---------------------")

add_by_10=[10,20,30,40,50]
s1 = pd.Series(data=add_by_10,name="Adding 10 for every element")
print(s1)
print("------------------")
print(s1.name)