'''
 @overload
def identity(n:
int,
             dtype:
None = ...,
             *,
             like: _SupportsArrayFunc = ...) -> ndarray[Any, dtype[floating[_64Bit]]]

If k value defined identi matrics start from der
K  0  1   2
 0  [[1. 0. 0.]
-1   [0. 1. 0.]
-2   [0. 0. 1.]]
'''

import  numpy as np
import sys

o=np.identity(3) # indentity with 3*3 matrice if 2 the 2*2
print(o)
print("--------------------------------")
o=np.identity(3,float) # if M specified the n row M cloumns
print(o)