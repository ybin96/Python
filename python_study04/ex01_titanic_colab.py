import matplotlib.pyplot as plt
import pandas as  pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('titanic')

# 3. 객실 등급에 따른 남여 생존율
df3 = df.dropna(subset=['sex', 'class', 'alive'])\
            .groupby(['class','sex'], as_index=False)\
            ['alive']\
            .value_counts(normalize=True)
print(df3)
df3 = df3.query('alive == "yes"')[['sex','class','proportion']]
print(df3)
sns.barplot(data=df3, x='class', y='proportion', hue='sex')
plt.show()



# 2. 객실 등급에 따른 생존자
# df2 =  df.dropna(subset=['class', 'alive'])\
#             .groupby('class', as_index=False)\
#             ['alive']\
#             .value_counts(normalize=True)
# print(df2)
# df2 = df2.query('alive=="yes"')
# print(df2)
#
# sns.barplot(data=df2, x='class', y='proportion')
# plt.show()



# print(df)
# 1. 성별별 생존율
#
# df1 = df.dropna(subset=['sex','alive'])\
#     .groupby('sex', as_index=False)\
#     ['alive']\
#     .value_counts(normalize=True)
# print(df1)
# df1 = df1.query('alive=="yes"')
# print(df1)
# sns.barplot(data=df1, x='sex', y='proportion')
# plt.show()
#


