
#in normal python

import  numpy as np

a = np.array([10,20,30])
b = np.array([1,2,3])
#dot production A.B=10*1 + 20*2 +30*3 = 140

#traditional python code
def dot_product(a,b):
    result = 0
    for i,j in zip(a,b):
        result = result +i*j
    return result

print(dot_product(a,b)) #140

output = np.dot(a,b)
print(output) #140