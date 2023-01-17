import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# print(titanic.head())
# print(titanic.info())
# print(titanic)

#who의 값의 종류별 빈도를 확인
print(titanic['who'].value_counts())
# man      537
# woman    271
# child     83

#다음의 3개의 그래프를 한 화면에 그려봅니다.                                       완성하면 "1"
#1. Class의 값의 종류별 빈도수
# sns.countplot(data=titanic, x='class')
# plt.show()

#2. Class의 값의 종류별 빈도수, who를 구분해 줍니다.
# sns.countplot(data=titanic, x='class', hue='who')
# plt.show()

#3. Class의 값의 종류별 빈도수, who를 구분해 주고 누적형태로 그립니다.
# sns.countplot(data=titanic, x='class', hue='who', dodge=False)
# plt.show()


fig = plt.figure(figsize=(15,5))
a = fig.add_subplot(1,3,1)
b = fig.add_subplot(1,3,2)
c = fig.add_subplot(1,3,3)

sns.countplot(data=titanic, x='class', ax=a)
sns.countplot(data=titanic, x='class', hue='who', ax=b)
sns.countplot(data=titanic, x='class', hue='who', dodge=False,  ax=c)
plt.show()












