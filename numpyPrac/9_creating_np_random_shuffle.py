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

o=np.random.randint(1,20,(4,4))                 #alway int
print(o)
np.random.shuffle(o)
print(o)