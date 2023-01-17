'''
--  ------       --------------  -----
 0   survived     891 non-null    int64
 1   pclass       891 non-null    int64
 2   sex          891 non-null    object
 3   age          714 non-null    float64
 4   sibsp        891 non-null    int64
 5   parch        891 non-null    int64
 6   fare         891 non-null    float64
 7   embarked     889 non-null    object
 8   class        891 non-null    category
 9   who          891 non-null    object
 10  adult_male   891 non-null    bool
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object
 13  alive        891 non-null    object
 14  alone        891 non-null    bool

'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())
print(df.info())

#두변수 사이의 관계             산점도
#나이와 요금의 관계를 산점도를 찍어 봅시다.

# sns.scatterplot(data=df, x='age', y='fare')
# plt.show()

# 산점도와 회귀선을 함께 그려주는 함수   =====> regplot
# sns.regplot(data=df, x='age', y='fare')
# plt.show()

#fit_reg=False      : 회귀선 X
# sns.regplot(data=df, x='age', y='fare', fit_reg=False)
# plt.show()

# seaborn의 스타일
# darkgrid, whitegrid, dark, white, ticks
sns.set_style('white')

#화면을 1행 2열로 분할하여 2개의 그래프를 그려 봅시다
fig = plt.figure(figsize=(15,5))      #화면의 가로크기, 세로크기를 설정합니다.

#fig를 1행 2열로 분리했을때의 1번째 화면을 ax1로 사용하겠다.
ax1 = fig.add_subplot(1,2,1)

#fig를 1행 2열로 분리했을때에 2번째 화면을 ax2로 사용하겠다.
ax2 = fig.add_subplot(1,2,2)

#첫번째 화면인 ax1에 그래프를 그려 봅니다.
sns.regplot(
    data=df,
    x='age',
    y='fare',
    ax=ax1
)

sns.regplot(
    data=df,
    x='age',
    y='fare',
    fit_reg=False,
    ax=ax2
)

plt.show()
















