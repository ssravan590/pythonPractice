'''
1. range(n)--->n values from 0 to n-1
range(4)--->0,1,2,3
2. range(m,n)--->from m to n-1
range(2,7)--->2,3,4,5,6
3. range(begin,end,step)
range(1,11,1)--->1,2,3,4,5,6,7,8,9,10
range(1,11,2)--->1,3,5,7,9
range(1,11,3)--->1,4,7,10
arange([start,] stop[, step,], dtype=None, *, like=None)
'''

import  numpy as np

seq=np.arange(10) #- -10
print(seq)

seq = np.arange(1,11)
print("with initial and end :",seq)

seq = np.arange(1,11,2) # initial + 2 till 11
print("initila , end with step :",seq)
print("--------------------------------")
seq = np.arange(1,12,2,dtype=float)
print("i want dtype as float :",seq)
print("shape :",seq.shape)
print("reshape :",seq.dtype)
print("ndim :",seq.ndim)




print("--------------------------------")
