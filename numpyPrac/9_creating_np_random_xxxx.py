'''
ef randint(self,
            low:
int,
            high:
int |
None = ...,
            size:
None = ...) ->
int
-----------------\

'''

import  numpy as np
import random

o=np.random.randint(1,20)                 #alway int
print(o)
o=np.random.randint(1,20,(2,2))
print(o)
o=np.random.randint(1,20,(2,10,10))
print(o)
print("-------------rand-------------------")
o=np.random.rand(1,5)
print(o)
print("-------------rand 2,2,2-------------------")
o=np.random.rand(2,2,2)
print(o)
print("-------------rand 2,2,2,2-------------------")
o=np.random.rand(2,2,2,2)
print(o)
print("--------------randn------------------")
o=np.random.randn(1,2,3)
print(o)
print("--------------------------------")
o=np.random.uniform()
print(o)
o=np.random.uniform(1,20)
print(o)
o=np.random.uniform(2,2,(2,3))
print(o)