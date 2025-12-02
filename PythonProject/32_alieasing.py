def myFunction():
    print("hi, its me")

def myName(name):
    print("hi :",name)
myFunction()
my=myFunction # function aliesing
my()
my()
m=myFunction()
m

myName('withoutAlies')
n=myName
n("withALies")
del n
myName("after")