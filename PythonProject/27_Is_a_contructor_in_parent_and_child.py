#If construtors are present in parent and child, if create child class object then only contructor of childe will be called
#only with Super method will be able to cßall super class contructor else not

class Pa:
    def __init__(self):
        print("I am parent class constructor ",id(self))
        self.a = 10


class Child(Pa): #is a relation just like extends in java
    def __init__(self):
        super().__init__()
        print("I am child class constructor ",id(self))
        self.b= 20

c = Child()
print(c.a) # error because parent class contructor is not called(if super is commented)
print(c.b)
