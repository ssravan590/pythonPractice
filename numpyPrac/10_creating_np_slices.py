

import  numpy as np

l1d = [1,2,3,4,5]
a1d= np.array(l1d)
print(a1d)
print("----------------slice for 1d------------")
#using slice
print(a1d[:]) # print all
print(a1d[2:a1d.size]) # from 2index to last
print(a1d[3:4])
print(a1d[::2]) # every 2nd element in an array
print(a1d[2:a1d.size:3])

#3array
l2d = [[1,2,3,4],[6,7,8,9]]
a2d = np.array(l2d)
print(a2d)
print("----------------slice for 2d------------")
#using slices of 2d array
print(a2d[:,:]) # all the elements
print(a2d[1:,1:2])
print(a2d[1:,:])

l3d = [[[1,2,3,4],[6,7,8,9],[10,11,12,13]],[[14,15,16,17],[18,19,20,21],[22,23,24,25]],[[26,27,28,29],[18,19,20,21],[22,23,24,25]]]
a3d = np.array(l3d)
print(a3d)
print("----------------slice for 3d------------")
print(a3d[1:,1:2,:])
print(a3d[:,1:2,:])
print("----------------slice for 22------------")
print(a3d[:2,2:,:])
