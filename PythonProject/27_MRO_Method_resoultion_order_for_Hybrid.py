#like java we have Object if class not extending here also the same concept

class P:
    def __init__(self):
        print("I am P")
    def m1(self):
        print(" I am from P M1")
    def m2(self):
        print(" I am from P M2")

class P1(P):
    def __init__(self):
        print("I am P1")
    def m1(self):
        print(" I am from P1 M1")
    def m2(self):
        print(" I am from P1 M2")

class P2(P):
    def __init__(self):
        print("I am p2")
    def m1(self):
        print(" I am from P2 M1")
    def m3(self):
        print(" I am from P2 M3")

class P3(P1,P2):
    def __init__(self):
        print("I am child")


#here MRO metho Resolution algo means which class method should be exectude 1st based on order (p1,p2)
#MRO of p3
print(P3.mro())
#[<class '__main__.P3'>, <class '__main__.P1'>, <class '__main__.P2'>, <class '__main__.P'>, <class 'object'>]
#above the order if incase a clash occured if will follow above order to give 1st prefernce
