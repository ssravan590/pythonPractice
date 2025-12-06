import pandas as pd
book = ['Python','Java','DS','C','Golang']

s = pd.Series(book)
print(type(s))
print(s)
print("---------------------")
book_dict = {0:'Python',1:'Java',2:'Go-Lang'}
s1 = pd.Series(data=book_dict)
print(s1)

s2 = pd.Series(data=('list','l1'))
print(s2)

s3 = pd.Series(data=[1,2,3,4,5,6])
print(s3)

s4 = pd.Series(data={1,2,3,4,5})
print(s4)