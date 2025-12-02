
from random import *

# random() : generates some float value b/w 0 and 1 (not inclusive)
print("some random number" , random())
for i in range(10):
    print(random())

#uniform() :  to generate random float value between 2 give numbers (not inclusive)
print("Uniform ",uniform(1,10))
for i in range(10):
    print(uniform(1,10))

#randint() : to generate integer b/w tqo given numbers (incluse)
print("Random int" ,randint(1,10))
for i in range(10):
    print(randint(1,10))

#randrange(begin,end,step): return a random number from range begin <=x < end
#beging to end-1
#begin is optional
#step is to increment for ex step is 2 then in will increment by 2
print("range from 0 to 9 is : ",randrange(0,10))
print("range from 1 to 10 is : ",randrange(1,11))
print("range from 0(default) to 10 is : ",randrange(11))
print(" range with step :", randrange(0,10,2)) # only even numbers
print(" range with step :", randrange(0,10,3)) # increate by 3
print(" range with step :", randrange(0,10,4)) # increate by 4

#choice() : wont generate random number but will get a random object from given sequence
list1 = ['A','B','C','D','E','F']
print ("Random choice :", choice(list1))

str='asdasdedsfdsfgrfgedghtg'
print("Random charectere : ",choice(str))

#generate Random OTP of 5 degit

print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9)) # o/p: 6 0 9 2 0
#generate Random OTP of 5 degit with white space

print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='') #o/p : 13589