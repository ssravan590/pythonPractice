class StaticVariabke:
    a=20 #static variable
    def __init__(self):
        StaticVariabke.b=20
    def m1(self):
        StaticVariabke.c=30
    @classmethod
    def m2(cls):
        cls.d=40
    @staticmethod
    def m3():
        StaticVariabke.e=40
print(StaticVariabke.a)
StaticVariabke.a= 30
print(StaticVariabke.a)
print(StaticVariabke.__dict__)
s = StaticVariabke()
print(StaticVariabke.__dict__)
s.m1()
print(StaticVariabke.__dict__)
StaticVariabke.m2()
print(StaticVariabke.__dict__)
print("Printing static variable",StaticVariabke.d)

