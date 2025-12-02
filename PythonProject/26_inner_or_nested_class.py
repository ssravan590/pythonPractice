class Outerclass:
    def __init__(self):
       print("I am outer class constructor")
    def display(self):
        print("I am method of outer class")
    class InnerClass:
        def __init__(self):
            print("I am inner class constructor")
        def display(self):
            print("I am inner class method")

o = Outerclass()
o.display()

i = o.InnerClass()
i.display()


