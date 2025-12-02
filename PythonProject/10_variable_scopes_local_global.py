from logging import makeLogRecord

globalA=10
def func1():
    print(globalA)

def func2():
    print(globalA)

def func3():
    a= 10
    print(a)

def func4():
    global globalA  #this will local variable refer to global variable
    globalA =111 # this will global variable now
    print(globalA)

def fun5():
    globalA=222 # this local now
    print(globalA)
def fun6():
     print(globalA)

def fun7():
    global makelocalvarglobal # this will now be reffered as global and not local
    makelocalvarglobal= 20
    print(makelocalvarglobal)
    print(type(makelocalvarglobal))

def fun8():
    print(makelocalvarglobal)


func1()
func2()
func3()
func4()
fun5()
fun6()
fun7()
fun8()

print(type(makelocalvarglobal))
a=10
for i in range(5):
    b=a
print(a + b)




