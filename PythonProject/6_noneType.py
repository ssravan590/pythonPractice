x=10
print(x)
x=None # x with 10 is now GC
print(x)

def fun():
    print("i am from fun")

returned =fun()
print("default type is :",returned)
print("type of None is :",type(returned))


def fun1():
   pass
print(fun1())