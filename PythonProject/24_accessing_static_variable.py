class AccessingStatic:
    a=20 #static variable
    def __init__(self):
        print("in constrct printing using self :",self.a)
        print("In constrct printing using className",AccessingStatic.a)
    def m1(self):
        print("in m1 printing using self :",self.a)
        print("In m1 printing using className",AccessingStatic.a)
    @classmethod
    def m2(cls):
        print("in m2 printing using cls   :",cls.a)
        print("In m2 printing using className",AccessingStatic.a)
    @staticmethod
    def m3():
        #print("in printing using self :",self.a)
        print("In m3 printing using className",AccessingStatic.a)
a = AccessingStatic()
print(AccessingStatic.__dict__)



