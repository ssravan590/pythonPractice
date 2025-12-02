'''
empty(shape: SupportsIndex | Sequence[SupportsIndex],
          dtype:
None = ...,
          order: Literal["C", "F"] |
None = ...,
          *,
          device: Literal["cpu"] |
None = ...,
          like: _SupportsArrayFunc |
None = ...) ->
ndarray[Any,
dtype[floating[_64Bit]]]
'''

import  numpy as np
import sys

o=np.empty((3,3))# input tuple
print(o)
o=np.empty([2,2])# input array
print(o)