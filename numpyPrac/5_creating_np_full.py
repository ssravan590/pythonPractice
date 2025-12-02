'''
 full(shape: SupportsIndex | Sequence[SupportsIndex],
         fill_value: Any,
         dtype:
None = ...,
         order: Literal["C", "F"] |
None = ...,
         *,
         device: Literal["cpu"] |
None = ...,
         like: _SupportsArrayFunc = ...) -> ndarray[Any, dtype[Any]]
o = np.zeros((2,3,4,5)) # 4 rows , 5 coulmns , 3 -- repeat for (4,5) three times , 2 - 3 for 2 times
'''

import  numpy as np
import sys

o=np.full((2,2),fill_value=2,dtype=int)
print(o)
print("--------------------------------")
o=np.full((2,2,2),fill_value=2,dtype=int)
print(o)
print("--------------------------------")
o=np.full((2,2,2,2),fill_value=2,dtype=str)
print(o)
print("--------------------------------")
o=np.full((2,2,2,2),fill_value=2,dtype=int)
print(o)
print("--------------------------------")