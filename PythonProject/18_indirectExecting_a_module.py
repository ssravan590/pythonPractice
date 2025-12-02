import test1 # this will indirect call test1 as main
print(__name__) # this will main and test1 __name__ will just give u module name
print(test1.name)
