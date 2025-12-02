from abc import abstractmethod
class Vehicle:
     @abstractmethod #if used mandatory to implement in child class
     def getNoOfWheels(self):
         pass
class Bus(Vehicle):
     def getNoOfWheels(self):
         print("I have 4 wheels")

b = Bus().getNoOfWheels()

