

import  numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print("-------------------------------")
for x in a:
    print(x)
    for y in x:
        print(y)
print("-------------------------------")

b = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(b)
print("-------------------------------")
for aa in b:
    for bb in aa:
        for cc in bb:
            print(cc)
print("-------------------------------")
