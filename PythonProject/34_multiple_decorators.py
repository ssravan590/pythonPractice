# decorator is function that takes function as arguments and extends its functionalities  and returns as modified function

def decor1(inputFunction):
    print("i am decor1")
    def inner1():
        print("i am executing decor1")
    return inner1

def decor2(inputFunction):
    print("i am docor2")
    def inner2():
        print("i am executing decor2")
    return inner2

@decor1
@decor2
def display():
    print("show as it isb")

@decor2
@decor1
def display_x():
    print("show as it is from display_x")

display()
#decor2 will be 1st executed and try to execute decor1 and since inner2 is not decor1 it will go to docor1
#deco1 will be executed and its inner function
print('x'*40)
display_x()