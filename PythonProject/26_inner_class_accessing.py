class Human:
    def __init__(self):
       print("I am Human class constructor")
       self.h=self.Head() # creating Head Object
    def display(self):
        print("I am method of Human class")
        self.h.display()
    class Head:
        def __init__(self):
            print("I am Head class constructor")
            self.b = self.Brain()
        def display(self):
            print("I am Head class method")
            self.b.display()
        class Brain:
            def __init__(self):
                print("I am Brain class constructor")
            def display(self):
                print("I am Brain class method")

o = Human()
o.display()



