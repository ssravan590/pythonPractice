#finding members of module using dir()
#using dir we can list members of a current module including default

from test1 import *
sum(1,3)
print(dir())

import math as m
print(dir(m))

############ help() ############
# dir returns all the member but we cannot find if it a variable or funtions to find if it is variable or function we go for help()

print(help(m))

#print(help()) in console enter module u get all the module