

import  numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print("-------------------------------")
for pos,ele in np.ndenumerate(a):
    print(f"position of {pos} and element {ele}")
print("-------------------------------")

b = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
for pos,ele in np.ndenumerate(b):
    print(f"position of {pos} and element {ele}")
print("-------------------------------")
