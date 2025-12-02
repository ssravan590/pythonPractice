'''
  eye(N:
int,
        M:
int |
None = ...,
        k:
int = ...,
        dtype:
None = ...,
        order: Literal["C", "F"] |
None = ...,
        *,
        device: Literal["cpu"] |
None = ...,
        like: _SupportsArrayFunc |
None = ...) -> ndarray[Any, dtype[floating[_64Bit]]]
 np.eye(2, dtype=int)
array([[1, 0],
       [0, 1]]
 np.eye(3, k=1)
array([[0.,  1.,  0.],
       [0.,  0.,  1.],
       [0.,  0.,  0.]])

If k value defined identi matrics start from der
K  0  1   2
 0  [[1. 0. 0.]
-1   [0. 1. 0.]
-2   [0. 0. 1.]]
'''

import  numpy as np
import sys

o=np.eye(3) # indentity with 3*3 matrice if 2 the 2*2
print(o)
o=np.eye(3,2) # if M specified the n row M cloumns
print(o)
o=np.eye(3,3,k=1) # if M specified the n row M cloumns
print(o)
print("--------------------------------")
o=np.eye(3,3,k=-1) # if M specified the n row M cloumns
print(o)