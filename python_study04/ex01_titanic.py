import matplotlib.pyplot as plt
import pandas as  pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('titanic')


# 다음을 분석 해 봅니다.                                              완성하면 "1"
# 4. 혼자 탑승한 사람과 가족과 함께 탑승한 사람의 생존율
# df4 = df.dropna(subset=['alone','alive'])\
#         .groupby('alone', as_index=False)\
#         ['alive']\
#         .value_counts(normalize=True)
# print(df4)
# df4 = df4.query('alive == "yes"')
# print(df4)
# sns.barplot(data=df4, x='alone', y='proportion')
# plt.show()


# 5. 배 요금에 따른 생존여부   ==> 생존자 수(비율)
print(df['fare'])
print(df['fare'].value_counts())

# df5 = df.dropna(subset=['fare','alive'])\
#     .groupby(['fare','alive'], as_index=False)\
#     .agg(n=('age','count'))
#
# print(df5)
# #          fare alive  n
# # 0      0.0000    no  6
# df5 = df5.query('alive=="yes"')
# print(df5)

#fare와 n의 관계
# sns.scatterplot(data=df5, x='fare', y='n')
# plt.show()

# 6. 연령별 생존여부
df6 = df.dropna(subset=['age','alive'])\
    .groupby(['age','alive'], as_index=False)\
    .agg(n=('who','count'))

print(df6)
#          fare alive  n
# 0      0.0000    no  6
df6 = df6.query('alive=="yes"')
print(df6)

sns.lineplot(data=df6, x='age', y='n')
plt.show()





# 3. 객실 등급에 따른 남여 생존율
# df3 = df.dropna(subset=['sex', 'class', 'alive'])\
#             .groupby(['class','sex'], as_index=False)\
#             ['alive']\
#             .value_counts(normalize=True)
# print(df3)
# df3 = df3.query('alive == "yes"')[['sex','class','proportion']]
# print(df3)
# sns.barplot(data=df3, x='class', y='proportion', hue='sex')
# plt.show()
#


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





