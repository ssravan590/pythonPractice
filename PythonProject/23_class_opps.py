class ClsDemo:
    a=10
    def __init__(self):
        self.b = 20
    def m1(self):
         print("Print contructor variable",self.b)
    @staticmethod
    def  staticMeth():
        print("i am static method :",ClsDemo.a)
        ClsDemo.b =20
    @classmethod
    def  classMethod(cls):
        cls.c=30

print(ClsDemo.__dict__)
c =ClsDemo()
c.m1()
print(ClsDemo.__dict__)
ClsDemo.staticMeth()
print(ClsDemo.__dict__)
ClsDemo.classMethod()
print(ClsDemo.__dict__)
