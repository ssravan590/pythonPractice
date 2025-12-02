import os.path

print(dir())
#['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print(__import__)
print(__build_class__)

# what is __doc__
# this holds documention string
# example : ''' document comments '''
''' documented comments '''
print("docs : ",__doc__)

# what is __file__
# if u what to know current file name
print("file name is :",__file__)
print("absolute path :",os.path.abspath(__file__))
print("absolute path :",os.path.dirname(__file__))
print("absolute path :",os.path.basename(__file__))


import test1 #this indirectly executes indirectly
print(__name__)




