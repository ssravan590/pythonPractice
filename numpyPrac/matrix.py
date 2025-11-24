import numpy as np

a = np.zeros((10,10)) # zeros with 10 rows and 10 coulmds
print("*******zero with 10*10")
print(a)
print("*******zero with 10*10")

a = np.arange(1,101) # 1d array from 1 to 19
print(a)
a = a.reshape((10,10)) # reshape will divide 10/10 and and create 10*10 matroce
print(a)
b= np.arange(1,11)
print(b)
b = b.reshape(2,5)
print("after reshape")
print(b)

d= np.identity(3)
print(d)
d = np.identity(10)
print(d)

