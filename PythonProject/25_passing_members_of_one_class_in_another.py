class Emp:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
    def display(self):
        print("display eno :",self.eno)
        print("display ename :",self.ename)

class Manager:
    def update(emp):
        emp.eno = 345
        emp.ename = "BCD"

e = Emp(123,"ABC")
e.display()
Manager.update(e)
e.display()

