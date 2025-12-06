

import  numpy as np

l1d = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,25]
a1d= np.array(l1d)
print(a1d)
cview = a1d[1:5]
print(cview)
cview[0]= 111
print(cview) #even updated in copy it will update in orginal as well
print(a1d)