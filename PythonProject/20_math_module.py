# working with math module
#sqrt(x)
#ceil(x)
#floor(x)
#fabs(x)
#log(x)
#sin(x)
#tan(x)

import  math as math

print("square root :",math.sqrt(2))
print("ceil of 10.1 :", math.ceil(10.1))
print("floor :", math.floor(10.2))
print("fabs :", math.fabs(10.2))
print("fabs :", math.fabs(-10.2)) # fabs : 10.2
print(math.fmod(1,2))

import random as random

list=[str(math.pi) for i in range(10)]
print(list)

list1=[str(round(math.pi)) for j in range(1,6)]
print(list1)

list2=[str(math.ceil(math.pi)) for j in range(1,6)]
print(list2)