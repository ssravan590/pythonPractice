'''
zeros(shape, dtype=float, order='C', *, like=None)
o = np.zeros((2,3,4,5)) # 4 rows , 5 coulmns , 3 -- repeat for (4,5) three times , 2 - 3 for 2 times
'''

import  numpy as np
import sys

o=np.zeros(3)
print(o)
print("--------------------------------")
o=np.zeros((5,5)) # shape 5 rows and 5 columns
print("dim :",o.ndim)
print("shaper :",o.shape)
print(o)
print("--------------------------------")
o = np.zeros((2,3,4))
print("dim :",o.ndim)
print("shaper :",o.shape)
print(o)
print("--------------------------------")
o = np.zeros((3,3,4))
print("dim :",o.ndim)
print("shaper :",o.shape)
print(o)
print("--------------------------------")
o = np.zeros((2,3,4,5)) # 4 rows , 5 coulmns , 3 -- repeat for (4,5) three times , 2 - 3 for 2 times
print("dim :",o.ndim)
print("shaper :",o.shape)
print("totl elements :",sys.getsizeof(o))
print(o)
print("--------------------------------")
o1 = np.ones((2,2))
print(o1)
print("--------------------------------")
o1 = np.ones((3,2,2),dtype=float)
print(o1)
print("--------------------------------")
o1 = np.ones((3,2,2),dtype=int)
print(o1)



