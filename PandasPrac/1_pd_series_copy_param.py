import pandas as pd
import numpy as np
book = ['Python','Java','DS']

s = pd.Series(data=book,copy=False)
print(s)
s[2] = 'C'
print("---------------------")
print(s)
print(book)
print("---------------------")

name_dict = {'S':'Sunny','B':'Bunny','D':'Don'}
s2 = pd.Series(data=name_dict,copy=True)
print(s2)
s2['D'] = 'King'
print(s2)
print(name_dict)
print("---------------------")

np.array(name_dict)

