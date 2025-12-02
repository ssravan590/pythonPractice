#int()
#float()
#complex()
#bool()
#str()


f = 111.111
print(int(f))
print(int(11.2))

print(int(True))
print(int('123'))

print(float(10))

#print(int(10+10j))

#complex
print(complex(10)) # 10 will be real part and imaginary part will be 0 so output is (10+0j)
print(complex(10,2)) # 10 will be real part and imaginary part will be 2 so output is (10+2j)
print(complex(True,False)) # 1 will be real part and imaginary part will be 0 so output is (10+2j)
print(complex(True)) # 1 will be real part and imaginary part will be 0 so output is (10+2j)
print(complex(10j)) # only imaginary part
print(complex(10.5,2.44))

print(bool('true'))
print(bool('yes'))
print(bool('1'))

print(str(111))
print(str(10+20j))