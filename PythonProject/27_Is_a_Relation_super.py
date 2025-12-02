from itertools import product


class Pa:
    def __init__(self):
        print("I am parent class constructor ")
    def m1(self):
        print("I am parent class instance method")
    @classmethod
    def m2(cls):
         print("I am parent class class methdd")
    @staticmethod
    def m3():
         print("I am parent class static method")

class Child(Pa): #is a relation just like extends in java
   pass

c = Child()

c.m1() # able to call parent class from child class
Child.m2()
Child.m3()
