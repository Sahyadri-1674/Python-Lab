import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(d)
print(df)

reqRow = df.loc[0]
print(reqRow)


df1 = pd.DataFrame({'W':[68,75,86,80,66],'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
df1=df1.add_prefix('pre_')
df1=df1.add_suffix('_suf')
print(df1)


sr1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
sr2 = pd.Series([1, 2, 3, 4, 5])

df2a = pd.DataFrame({'Languages':sr1,'Number':sr2})
print(df2a)

df2b = pd.concat([sr1,sr2],axis=1)
print(df2b)

import numpy as np
sdata = {"c1":[120, 130 ,140, 150, np.nan, 170], "c2":[7, np.nan, 10, np.nan, 5.5, 16.5]}

df3 = pd.DataFrame(sdata)
print(df3)

#df3.fillna('missing',inplace=True)
#df3.fillna(method='pad',inplace=True)
df3.fillna(method='bfill',inplace=True)
print(df3)


exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew','Raj','Sharad','Arvind']
,'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data,index=labels)
#df = pd.DataFrame(exam_data)
print("Original DataFrame")
print(df)
#print("\nSet a given value for particular cell in the DataFrame")
#df._set_value(8,'score',10.2)
#print(df)

print(df.loc[df['score'].between(15,20)])
             
