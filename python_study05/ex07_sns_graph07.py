import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

#distplot : 단변수(하나의 변수)에 사용하며, 기본값은 히스토그램과 커널 밀도 함수(확률 밀도)를 그래프로 출력합니다.

#요금에 대하여 히스토그램과 커널 밀도 함수를 그래프로 그려 봅시다.
# sns.displot(data=titanic,x='fare' )
# hist  히스트그램 표시여부
# kde   커널 밀도 함수 표시 여부
# sns.distplot(titanic['fare'])   
# plt.show()

fig = plt.figure(figsize=(15,5))
a = fig.add_subplot(1,3,1)
b = fig.add_subplot(1,3,2)
c = fig.add_subplot(1,3,3)

sns.distplot(titanic['fare'], ax=a)
sns.distplot(titanic['fare'], ax=b,hist=False )
sns.distplot(titanic['fare'], ax=c,kde=False)
plt.show()


# 다음의 3개의 그래프를 한 화면에 그려 봅니다.                완성하면 "3"
# 1. 요금에 대한 히스트그램과 커널밀도 함수
# 2. 요금에 대한 커널 밀도 함수
# 3. 요금에 대한 히스토 그램











