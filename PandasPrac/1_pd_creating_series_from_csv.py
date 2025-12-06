import pandas as pa
import pandas as pd

df = pa.read_csv('students.csv')
print(type(df))
print(df)

#-------------------------
df = pa.read_csv('students.csv', usecols=['Name of Student'])
print(df)
#------------------to convert DataFrame object it series use squeeze are true
#df = pa.read_csv('students.csv', usecols=['Name of Student'], squeeze=True)
#print(type(df))
df = pa.read_csv('students.csv', usecols=['Name of Student','Marks'])
print(df)

#print(df)
print('Type of :', type(df))
#dfs=df.squeeze()
#print("Type of :",type(dfs))
#print(df.head(10))
#print(df.isna)
s =df['Marks']
print(type(s))
print(s.hasnans)
print(s.count())
print(s.tail(20))
#print(s.head(20))
print("count of null",s.isnull().count())
print("sum of null ",s.isnull().sum()) # how many null values
print("count of na",s.isna().count())
ss = s.fillna("000")
print(ss)
print(s)
sd = s.dropna()
print(sd)
#sda =s.dropna(inplace=True)
#print(sdaz)
print(s)

sdm = s.fillna(s.mean())
print(sdm)
sdmedian = s.fillna(s.median())
print(sdmedian)



print("Mean :",s.mean())
print("Median :",s.median())
print("variance :",s.var())
print("stand deviation ", s.std())
print("mode :",s.mode())
print("value counts",s.value_counts()) # retuns hoe many time a value is repeated
print("max :",s.max())
print("min :",s.min())
print("idxmin :",s.idxmin())

print("describe :",s.describe())
sv = s.sort_values()
print(sv)



l1 = [10,20,30,40]

s1= pd.Series(l1,index=[1,2,3,4])
s2= pd.Series(l1,index=[2,4,6,8])
print("---------------------")
s3 = s1.add(s2)
print(s3)
s4= s1.add(s2,fill_value=0)
print(s4)

print(s1.cummax())
print(s1.cumprod())

print("S1 is :", s1)
print(s1.diff()) # deference with 1st previous element
print(s1.diff(periods=2)) # difference with 2nd previous element
print(s1.diff(periods=-1)) # differnce with next emlement

