#boxplot  : 범주형 데이터의 분포와 주요 통계자료를 제공하는 함수입니다.
#                   boxplot만으로는 데이터의 퍼져있는 분산정도를 정확하게 파악하기에는 어려워요
#violinplot     을 이용하면 퍼져있는 분산정도를 시각적으로 파악할 수 있어요

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 다음의 4개의 그래프를 한 화면에 그려 봅니다.            완성하면 "1"
# 첫번째행에는 나이에 따른 생존자의 분포를 boxplot으로 그립니다. 오른쪽에는 성별이 구분되도록 합니다.
# 첫번째행에는 나이에 따른 생존자의 분포를 violinplot으로 그립니다. 오른쪽에는 성별이 구분되도록 합니다.

fig = plt.figure(figsize=(15,15))
fig11 = fig.add_subplot(2,2,1)
fig12 = fig.add_subplot(2,2,2)
fig21 = fig.add_subplot(2,2,3)
fig22 = fig.add_subplot(2,2,4)

sns.boxplot(data=titanic, x='alive',y='age',ax=fig11)
sns.boxplot(data=titanic, x='alive',y='age',hue='sex', ax=fig12)
sns.violinplot(data=titanic, x='alive',y='age',ax=fig21)
sns.violinplot(data=titanic, x='alive',y='age',hue='sex', ax=fig22)
plt.show()


# sns.boxplot(data=titanic, x='alive', y='age')
# sns.violinplot(data=titanic, x='alive', y='age')
# plt.show()



