import pandas as pd
book = ['Python','Java','DS','C','Golang']

s = pd.Series(book)
print(s[0])
print(s.iloc[0]) # both s[0] is same but iloc is more has good performance
print(s.iloc[[1,3]])
print("-----------with slice--------------")
print(s.iloc[:])
print(s.iloc[2:4])

print("---------------loc for labled based selection")
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
s = pd.Series(data=alpha,index=["Label_"+x for x in alpha])
#s1 = s.add_suffix("Index_")
print(s)
print(s.loc['Label_S'])
print(s.loc['Label_X'])
print(s.loc[['Label_S','Label_R','Label_A']])
print(s.loc['Label_A':'Label_N'])