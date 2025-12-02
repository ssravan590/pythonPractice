from itertools import product


class P1:
    def __init__(self):
        print("I am P1")
    def m1(self):
        print(" I am from P1 M1")
    def m2(self):
        print(" I am from P1 M2")

class P2:
    def __init__(self):
        print("I am p2")
    def m1(self):
        print(" I am from P2 M1")
    def m3(self):
        print(" I am from P2 M3")

class C(P1,P2):
    def __init__(self):
        print("I am child")

c = C()
c.m1() # P1 m1 becaus p1 is ordered 1st
c.m2()
c.m3()

