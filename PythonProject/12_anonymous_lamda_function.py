def square(n):
    return n*n

print(square(2))

#lamda
value=lambda n:n*n
print(value(2))
print(value(3))

print(type(value))
sumIs=lambda a,b:a+b

print(sumIs(10,10))

bg=lambda a,b:a if a>b else b

print(bg(10,20))

bg3 = lambda a,b,c : a if a>b and a>c else b if b>c else c

print(bg3(20,3,30))