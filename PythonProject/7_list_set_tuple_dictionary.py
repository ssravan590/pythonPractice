from multiprocessing.managers import Array

l=[1,2,3,4,4,5,'asdas']
print("List of element", l)
l.append(12)
print("List of element", l)
l.remove('asdas')
print("List of element", l)
print("1st number", l[0])
print("last number", l[-1])
print("Lenght", len(l))


s={1,2,3,4,4,5,'asdasd'}
print("set :",s)
s.add(12)
print("set :",s)
s.remove(12)
print("set :",s)
print("Lenght", len(s))

t=(1,2,3,4,5)
print("tuple :",t)
print(t[0])        # slicing is applicable for tuple
#t[0] = 'asdasd' #not applicable
print(t[0:3])
print("Lenght", len(t))

# tupple immutable

d ={'a':123,'b':123}
print("dictionary :",d)
print(d.get('a'))
d['a']=545454
print(d)

listA=[x for x in range(100)]
print(listA)
print(type(listA))

genertorA=(x for x in range(100))
print(genertorA)
print(type(genertorA))