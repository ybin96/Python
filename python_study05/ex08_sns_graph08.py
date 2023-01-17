import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')

#jointplot : 산점도를 기본으로 표시하고 x-y축에 각 변수에 대한 히스트그램을 동시에 보여 주는 함수입니다.
#               두변수 사이에 관계와 값의 분포도(데이터가 분산되어 있는 정도)를 한눈에 확인 할 수 있어요!

#x:fare, y:age  에 대하여 산점도와 히스토그램을 동시에 확인 해 봅시다.
#회귀선 : kind="reg"
#육각 산점도 : kind="hex"
#커널밀도함수    : kind="kde"
# sns.jointplot(data=titanic, x='fare', y='age')
# sns.jointplot(data=titanic, x='fare', y='age', kind='reg')
# sns.jointplot(data=titanic, x='fare', y='age', kind='hex')
sns.jointplot(data=titanic, x='fare', y='age', kind='kde')
plt.show()