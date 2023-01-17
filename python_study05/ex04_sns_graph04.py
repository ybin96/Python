import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic.head())
print(titanic.info())

# alive, survived
#다음의 3개의 그래프들을 한 화면에 그려 봅니다.            완성하면 "1"

fig = plt.figure(figsize=(20,5))
a = fig.add_subplot(1,3,1)
b = fig.add_subplot(1,3,2)
c = fig.add_subplot(1,3,3)
sns.barplot(data=titanic, x='sex',y='survived', ax=a)
sns.barplot(data=titanic, x='sex', y='survived', hue='class',ax=b)
sns.barplot(data=titanic, x='sex', y='survived', hue='class', dodge=False, ax=c)
plt.show()


#1. 성별별로 생존자의 수를 막대그래프로 그립니다.
# sns.barplot(data=titanic, x='sex',y='survived')
# plt.show()

#2. 성별별로 생존자의 수를 막대그래프로 그립니다. class를 구분해서 표시합니다.
# sns.barplot(data=titanic, x='sex', y='survived', hue='class')
# plt.show()

#3. 성별별로 생존자의 수를 막대그래프로 그립니다. class를 구분해서 표시하고 누적 막대로 그립니다. (dodge=False)
# sns.barplot(data=titanic, x='sex', y='survived', hue='class', dodge=False)
# plt.show()


#성별별로 생존자의 수를 요약표를 만들어요
# df1 = titanic.groupby('sex',as_index=False)\
#         ['alive']\
#         .value_counts()
# df1 = df1.query('alive == "yes"')
# print(df1)
#
# sns.barplot(data=df1, x='sex', y='count')
# plt.show()

#2. 성별별로 생존자의 수를 막대그래프로 그립니다. class를 구분해서 표시합니다.
# df2 = titanic.groupby(['sex','class'], as_index=False)\
#         ['alive']\
#         .value_counts()
# df2 = df2.query('alive == "yes"')
# # print(df2)
# sns.barplot(data=df2, x='sex',y='count',hue='class' )
# plt.show()


#3. 성별별로 생존자의 수를 막대그래프로 그립니다. class를 구분해서 표시하고 누적 막대로 그립니다. (dodge=False)
# df3 = titanic.groupby(['sex','class'], as_index=False)\
#         ['alive']\
#         .value_counts()
# df3 = df3.query('alive == "yes"')
# # print(df2)
# sns.barplot(data=df3, x='sex',y='count',hue='class', dodge=False )
# plt.show()
