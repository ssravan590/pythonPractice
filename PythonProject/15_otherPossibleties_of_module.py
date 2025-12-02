#module aliesing "as"
#using 'from' we can get what is required and use it directly
import test as t
print(t.name)
print(t.mul(10,2))

from test import name # only name
print(name)



from test import mul as m , sum as s
print(m(10,10))
print(s(1,1))

from test import * # only name
print(sum(10,20))



from test import *
from test1 import *
print(sum(10,10)) # add function is available in test and test1 but latest import of test1 will override here