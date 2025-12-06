

import  numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print("-------------------------------")
for x in np.nditer(a):
    print(x)

print("-------------------------------")

b = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(b)
print("-------------------------------")
for aa in np.nditer(b):
   # for bb in np.nditer(aa):
    #    for cc in np.nditer(bb):
            print(aa)
print("-------------------------------")
for yy in np.nditer(a[:,:2]):
    print(yy)
