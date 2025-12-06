

import  numpy as np

a = np.array([1,2,3])
b = np.array([4])
# shape of a is 3 and b in 1 so if we try to add both it fail with below error non matching shape
# so internally it to work it apply broadcasting rule by adding so b will be [4,4,4]  so [1,2,3] and [4,4,4]
print(a+b)

a1 = np.array([[1,2],[3,4],[5,6]])
b1 = np.array([10,20])
# interall by Braod casting will happend
print(a1+b1)

