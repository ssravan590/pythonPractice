def sum(a,b):
    return a+b

def mult(a,b):
    print(a*b)

def passFunc(a,b):
    pass

def stringFunc(a='hello ',b=' guest'):
    print("string : ",a,b)

def tupleFunction(*x):
    print("type of x",type(x))
    print("elements :" ,x)
    print('number of args ', len(x))

def sumTuple(*b):
    totnum =0
    for n in b:
        totnum = totnum + n
    print("sum of all number :" , totnum)

def dictTyple(**kwargs):
    print(type(kwargs))
    print(kwargs)


print(sum(10,20)) # positional arguments
mult(10,20)
passFunc(1,1)

print(sum(a=20,b=10))
print(sum(b=10,a=20))  # order is not important if variable name is specified such type argument are keyword args

print(sum(10,b=20))
#print(sum(10,a=20)) not allowed

print(stringFunc()) # posible because default arguments are in declaration of functions
print(stringFunc(b="Sravan"))
print(stringFunc("hai","namesthe"))

#var length arguments concept
tupleFunction()
tupleFunction(10)
tupleFunction(10,20,30)

sumTuple()
sumTuple(10,20,30)

dictTyple(name='sravan',company='NC',id=123)
# **kwargs : a group of key value pair args
# *args :  grouup of args


def display(**kwards):
    for k,v in kwards.items():
        print('{}={}'.format(k,v))
        print(kwards.get(k))

display(name='sravan',company='NC',id=123)