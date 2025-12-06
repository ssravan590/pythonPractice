

import  numpy as np

l1d = [1,2,3,4,5]
a1d= np.array(l1d)
print(a1d)
bool_array=np.array([True,False,True,False,True])
print(bool_array)

#conditional based array
print(a1d[bool_array])

cond = a1d > 2

print(a1d[cond])
print(a1d[a1d>3])

a = np.array([-12,-2,4,5,-6,12,234,-54,6,65767,3,43,5467,-7,-8,])

#select all negivitive elements
neg = a[a<0]
print(neg)

b = np.arange(1,26).reshape(5,5)
print(b)
print(b[b%2==0])
