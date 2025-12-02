#filter() -- filter based on given sequence with some condition
#syntax filter(function,variableName) function should return boolean
from functools import reduce

l=[0,5,10,12,15,17,18]

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

output=list(filter(is_even,l))
print(output)

#same with lambda
evens=list(filter(lambda n:n%2==0,l))
print(evens)
odds=list(filter(lambda n:n%2!=0,l))
print(odds)

#with tuples
t=('A','AA','AAA','AAAA')

outputT=tuple(filter(lambda s:len(s)>=3,t))
print(outputT)


############### map()
def squareOfNum(n):
     return n*n

l=[1,2,3,4,5]
l1=[2,3,4,5]
outputSquare=list(map(squareOfNum,l))
l2=list(map(lambda a,b:a*b,l,l1))
print(outputSquare)
print(l2)

outputSquarewithlambda=list(map(lambda n:n*n,l))
print(outputSquarewithlambda)

########  reduce() ########## this not available by defaul we need to import it from functools
r1=[10,20,30,40,50]

r2=reduce(lambda x,y:x+y,l)
print(r2)

r3=reduce(lambda x,y:x+y,range(1,101))
print(r3)

def mul(a,b):
    return a*b
r4=reduce(mul,r1)
print(r4)