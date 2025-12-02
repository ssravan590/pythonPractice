# decorator is function that takes function as arguments and extends its functionalities  and returns as modified function

def smart_division(inputfunction):
    def inner(a,b):
        if b == 0:
          print('hey, dividing with zero? sorry not possible')
        else:
          inputfunction(a,b) #call the existing function
    return inner

@smart_division #decorator function name should match
def divided(a,b):
    c = a/b
    print("output is :",c)

@smart_division #decorator function name should match
def modulus(a,b):
    c = a%b
    print("output is :",c)
divided(1,0)
divided(2,2)
modulus(1,0) # with decorator we are able to extend the existing function logic
