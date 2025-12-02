class Engine:
    def useEngine(self):
        print("Engine speacfic feature")
class Car:
    def __init__(self):
        self.engine=Engine() # Has a relation
        print("Engine feature added")
    def useCar(self):
        print("car required engine to start so using engine" )
        self.engine.useEngine()
        print("starting car")

c=Car()
c.useCar()