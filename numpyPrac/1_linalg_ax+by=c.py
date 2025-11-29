# x --> num of boys
# y --> num of girls
# linalg   x+y=2200 and 3x+8y=10100
# so from coefficient is [1,1],[3,8] and value is [2200,10100]
#what is x and y?

import numpy as np
a = np.array([[1,1],[3,8]])
b = np.array([2200,10100])
print("coffient is :",a)
print("value is :",b)

output = np.linalg.solve(a,b)
print("output is :",output) # output is : [1500.  700.]
# so x is 1500 and y = 700
print(type(output)) #<class 'numpy.ndarray'>