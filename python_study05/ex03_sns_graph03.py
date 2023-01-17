import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')
# print(titanic)

#stripplot: 범주형 변수에 들어 있는 각 범주별 데이터의 분포를 확인 할 수 있어요

#그래프의 스타일을 설정합니다.
sns.set_style('whitegrid')

fig = plt.figure(figsize=(5,15))
a = fig.add_subplot(2,1,1)
b = fig.add_subplot(2,1,2)

sns.stripplot(data=titanic, x='class',y='age',ax=a)
sns.swarmplot(data=titanic, x='class',y='age',ax=b)
plt.show()


#연습) 한 화면에 stripplot, swarmplot을 한번에 그려 봅니다.       완성하면 "3"


#나이와 클래스별로 데이터의 분포를 확인 해 봅시다.
# sns.stripplot(
#     data=titanic,
#     x='class',
#     y='age'
# )
#
# plt.show()
#동일한 값이 많을 경우 점이 찍힌데에 또 찍혀요!
#여기에 값이 더 많이 분포되었는지 파악하기가 어려워요
# ====> swarmplot

# sns.swarmplot(
#     data=titanic,
#     x='class',
#     y='age'
# )
# plt.show()



