# decorator is function that takes function as arguments and extends its functionalities  and returns as modified function

def decorFunction(inputFunction):
    def outputFunc():
        print("i am executing outputfunc")
    return outputFunc

@decorFunction  #decorator function name should match
def display():
    print("show as it isb")

display() # output is "i am executing outputfunc"


def decor_for_add(fun):
  def fun(x,y):
    print(x+y)
  return fun
@decor_for_add
def add(a,b):
    pass

add(1,2)