l1=[1,2,3,4]
l2=[5,6,7,8]

l3=[*l1,*l2]
l4= l2 + l3

print(" combined 2 list :" , l3)
print(" combined 2 list using +:" , l4)

s1={1,2,3,4}
s2={5,6,7,8}

s3={*s1,*s2}
s4={*l1,*l2}
print(" combined 2 set :" , s3)
print(" combining list to set ", s4)

l5= {*s1,*l1,*l3}
print(" combining set in to list ", l5)


t1=(1,2,3,4)
t2=(5,6,7,8)

t3=(*t1,*t2)
t4=t1 + t3
print("combining 2 tupple",t3)
print("combining 2 tupple",t4)


d1 ={1:'qw',2:'wer'}
d2={3:'wre',4:'asdasd'}

d3={**d1,**d2}

print("combining dict", d3)
# we cannot use d3={*d1,*d2} because it will treat as set not dict

lt =[(1,2,3),(4,5,6)]
print(lt[0][1])
print(lt[1][2])

dt = {
    'cars':('i10','i20'),
    'mobile':('nokia','apple','samsung')
}

print(dt)
print(dt['cars'][1])
print(dt.get('cars')[1])