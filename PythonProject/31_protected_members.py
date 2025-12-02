# by default all class members are public
# __ is used for private members


class ProtectedVariable:
    x = 10 #public variables
    __x = 20  #private varable
    _x = 30 # protected varable
    def m1(self):
       print("Public :",self.x)
       print("private : ",self.__x)
       print("protected : ", self._x)
       self.__m1()
    def __m1(self):
       print("Public :",self.x)
       print("private : ",self.__x)
       print("protected : ", self._x)
    def _m1(self):
       print("Public :",self.x)
       print("private : ",self.__x)
       print("protected : ", self._x)

p =ProtectedVariable()
print("Public :", p.x)
#print("private : ", p.__x)
print("protected is: ",p._x)
p.m1()
#p.__m1()






