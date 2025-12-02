def f1(function):
    print("f1 function got function argule",format(function))
    function()

def fx():
    print("fx function")

def fy():
    print("fy function")



f1(fx) # for f1 function pass fx function to get executed using aliesing
f1(fy)
#in python