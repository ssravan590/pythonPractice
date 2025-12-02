from itertools import product


class P1:
    def __init__(self):
        print("I am P1")
    def m1(self):
        print(" I am from P1 M1")
    def m2(self):
        print(" I am from P1 M2")

class P2(P1):
    def __init__(self):
        print("I am p2 constructor calling m1 from parent and self")
        super().m1()
        self.m1()
        super().__init__()
    def m1(self):
        print(" I am from P2 M1")


c = P2()


