import pandas as pd
book = ['Python','Java','DS']

s = pd.Series(data=book,index=['P','J','D'])

print(s)
print("---------------------")
#dulicate index labels also possible
s1 = pd.Series(data=book,index=['P','J','J'])
print(s1)
print("---------------------")
name_dict = {'S':'Sunny','B':'Bunny','D':'Don'}
s2 = pd.Series(data=name_dict)
print(s2)
print("---------------------")
s3 = pd.Series(data=name_dict,index=['S','B']) #only match idex will be taking
print(s3)
print("---------------------")
s4 = pd.Series(data=name_dict,index=['S','B','Z','D']) #Z does not exist so value will NaN
print(s4)