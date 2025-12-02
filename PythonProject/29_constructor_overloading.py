# same operator for muliple surposes call operator oveloading
class ConstructorOverloading:
     def __init__(self,x=None,y=None,z=None):
         print("default|one arg|2 arg")

c = ConstructorOverloading()
c1 = ConstructorOverloading(1)
c2 = ConstructorOverloading(11,2)


class ConstructorOverloadingDemo:
    def __init__(self, *args):
        print("default|one arg|2 arg")
        for i in range(len(args)):
            print("args :",args[i])


c11 = ConstructorOverloadingDemo()
c111 = ConstructorOverloadingDemo(1)
c21 = ConstructorOverloadingDemo(11, 2)
c22= ConstructorOverloadingDemo(1,2,1,2,1,2)
