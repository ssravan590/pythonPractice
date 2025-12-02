#slice operation:
#- slice is a part of string
#- how to pull a slice s[begin:end]
#being : from the index where we want to start with
#end: till which index
#  index 012345   is equal -5,-4,-3,-2,-1
s='1234567890'

#example for s[beign:end]
print(s[0:6])
print(s[3:8]) # begin to end -1
print(s[9]) # last index
print(s[-1]) # last index
print(s[:]) #we will all
print(s[:9]) #begin will start from 0
print(s[3:]) # if end is not specfied but default it will lates last

s1="kotasravan"
print(s1[-1])
print(s1[0].upper() +" "+ s1[4:len(s1)])
print(s[-3:-1])
print(s[:-1])

print(2*'Sravan') # two time for string resvers is alos same
#print('s'*'r') not valid
#s[begin:end:step]

print( s1[0].upper() +" "+ s1[-6:-1] + s1[-1]) #Sravan
