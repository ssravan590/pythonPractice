from traceback import print_tb

import numpy as np
#help(np)

l = [1,2,3]
print(type(l))
a = np.array(l)
print(a)   #1D array [1 2 3]
print(type(a))
print(a)
print("--------------------")
print("dim :",a.ndim) # to find dimention of ndarray 1d array
print("type :",a.dtype) # int64 type
print("shape :",a.shape) #shape of array # 3,1
print("--------------------")

twodArray = np.array([[1,2,3],[1,2,3],[1,2,3]])
print(twodArray)
print("dim :",twodArray.ndim) # to find dimention of ndarray 2dim
print("type :",twodArray.dtype) # int64 type
print("shape :",twodArray.shape) #shape of array #(3, 3)
print("--------------------")
twodArray2 = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4]])
print(twodArray2)
print("Dim :",twodArray2.ndim) # to find dimention of ndarray 2dim
print("dtype :",twodArray2.dtype) # int64 type
print("shape :",twodArray2.shape) #shape of array #(3, 4)
print("--------------------")
arrayofTuple1 =np.array(('q','d','e'))
arrayofTuple =np.array((('q','d','e'),('q','d','e')))
print(arrayofTuple)
print("Dim :",arrayofTuple.ndim) # to find dimention of ndarray 2dim
print("dtype :",arrayofTuple.dtype) # int64 type
print("shape :",arrayofTuple.shape) #shape of array #(3, 4)
print("--------------------")
arraywithFloat =np.array([[1,2,1.2],[1,2,3]])
print(arraywithFloat)
print("Dim :",arraywithFloat.ndim) # to find dimention of ndarray 2dim
print("dtype :",arraywithFloat.dtype) # dtype : float64 upcasting will be done becuase of float values
print("shape :",arraywithFloat.shape) #shape of array #(3, 4)

print("--------------------")
arraycustomType =np.array([[1,2,1],[1,2,3]],dtype=float)
print(arraycustomType)
print("dtype :", arraycustomType.dtype) #float64

print("--------------------")
arraycustomBool =np.array([[1,2,1],[1,2,0],[1,0,3]],dtype=bool)
print(arraycustomBool)
print("dtype :", arraycustomBool.dtype) #dtype : bool

print("--------------------")
arraycustomBool =np.array([[1,2,1],[1,2,0],[1,0,3]],dtype=str)
print(arraycustomBool)
print("dtype :", arraycustomBool.dtype) #dtype : <U1
#homeginous elements
hm = np.array([10,'aa',True,(10+9j),10.5],dtype=object)
print(hm)
print("dtype :", hm.dtype)
#[10 'aa' True (10+9j) 10.5]
#dtype : object


