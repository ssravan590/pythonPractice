# by default all class members are public
# __ is used for private members


class PrivateVariable:
    x = 10 #public variables
    __x = 20  #private varable
    def m1(self):
       print("Public :",self.x)
       print("private : ",self.__x)
       self.__m1()
    def __m1(self):
       print("Public :",self.x)
       print("private : ",self.__x)

p =PrivateVariable()
print("Public :", p.x)
#print("private : ", p.__x)
p.m1()
#p.__m1()






