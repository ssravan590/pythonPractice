import pandas as pd

names = ['A','B','C','D','E']
number = [10,2,3,4,5,64,33,44,55,66788,55,45,667]
s = pd.Series(data=number)
s1 = pd.Series(data=names)
print(s1[[True,False,True,True,False]])
def even_select(input):
    return [True if value%2 == 0 else False for value in input]

print(even_select(s))
print(s[even_select(s)])