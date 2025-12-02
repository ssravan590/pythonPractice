class Parent:
    def m1(self):
        print("I am parent class m1 method")

class Child(Parent): #is a relation just like extends in java
    def m2(self):
        print("I am from child class")

c = Child()
c.m1() # able to call parent class from child class
c.m2()