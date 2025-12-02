class InnerMethod:
    def m1(self):
        def cal(a,b):
            print("Sum :",a+b)
            print("Mult :",a*b)
            print("diff :",a-b)
        cal(2,1)

i = InnerMethod()
i.m1()


