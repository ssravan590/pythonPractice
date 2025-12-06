import pandas as pd
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
s = pd.Series(alpha,index=alpha)
print(s)
#s = s.add_prefix("Label_")
s = s.add_suffix("_Lable")
print(s)
print(s["Z_Lable"])


lable_list = list("lable_"+x for x in alpha)
print(lable_list)
print(list(map(lambda  x : 'Lable_'+x,alpha)))