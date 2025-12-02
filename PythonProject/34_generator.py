def mygen():
    yield 'A'
    yield 'B'
    yield 'c'

g = mygen()
print(type(g))

#print(next(g)) # A
#print(next(g)) # B
#print(next(g)) # c
#print(next(g)) # error
for x in g:
    print(x)

