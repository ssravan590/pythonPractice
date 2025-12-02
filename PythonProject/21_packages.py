#packages :
#A collecting of related module into a folder is package
#it is encapsulation mechanisam
#if a folder has __init__.py then only is it is considered as a package (example see programs folder left side) else not
#package if sub package also __init__.py should created only then subpackage is a package else not
#from Python3.2 __init__.py is not mandatory but recomanded
# how to demo1.py from program > example package
import programs as p
from programs.demo2 import *
from programs.example.demo1 import fun as a
from programs.example import *

fun()
a()
#print("printing x",x)
print("printing x from program package ",p.x)


#importance of __init__.py file
 #at the time of using a package, if we want to perform any initialization activities the we have to go for __init__.py file