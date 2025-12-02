# same operator for muliple surposes call operator oveloading
class Operator1:
    def __init__(self,pages):
      self.pages = pages
    def __add__(self,other):
        total_pages=self.pages+other.pages
        return total_pages

c1 = Operator1(2)
c2 = Operator1(2)

#print(c1+c2) # operator overloading is not directly possible to make this happen us have to use magic methods
#magic method here is __add__
print(c1+c2)


