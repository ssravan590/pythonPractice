

import  numpy as np


print("----------------1d array advanced slice------------")
array = np.arange(10,101,10)
idex = [2,5,9]
print(array)
print(array[idex]) # this returns values of array at index 2,5,9
#accessing directed
print(array[[-2,-1]])
print(array[[0,-1]])

print("----------------2d array advanced slice------------")
ar2d = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]])
print("----------full array------------")
print(ar2d)
print("--------------------------------")

print(ar2d[[0,1,2,3],[0,1,2,3]])
print(ar2d[[0,1,2,3],[1,3,0,2]])
print(ar2d[[0,1,2,3,3,3,3],[0,0,0,0,1,2,3]]) # L shape
print(ar2d[[0,1,2],[0]])

print("----------------3d array advanced slice------------")
ar3d = np.array([[[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]],[[1,2,3,4],[4,5,6,7],[7,8,9,10],[10,11,12,13]]])
print("----------full array------------")
print(ar3d)
print("--------------------------------")
print(ar3d[[0,1],[1,1],[2,1]])