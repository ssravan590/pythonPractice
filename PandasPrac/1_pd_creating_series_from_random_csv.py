import pandas as pa

df = pa.read_csv('annual-enterprise-survey-2024-financial-year-provisional.csv',
                 usecols=['Variable_name','Value'])

#print(df)
#print('Type of :', type(df))
df1 = pa.read_csv('annual-enterprise-survey-2024-financial-year-provisional.csv')
print(df1.filter(regex='^V'))
print(df1.filter(like='Val'))

print(df.where())