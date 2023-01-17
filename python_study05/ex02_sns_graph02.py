import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
# print(titanic)


# heatmap : 2개의 범주형 변수에 대하여 각각 x,y 축에 놓고
# 데이터를 메트릭스 형태로 분류해 주는 그래프입니다.
# x:class, y:sex, 사람수

# 히트맵을 그리기 위한 피벗테이블을 만들어요
df = pd.pivot_table(data=titanic, index='sex', columns='class',aggfunc='size')
print(df)

sns.heatmap(data=df,
            annot=True,              #값을 표시
            fmt='d',                 #지수형태로 나타나는 값을 정수로 표시
            linewidths=2,            #구분 선 두께
            cmap='coolwarm',         #colormap 설정
            cbar=False               #칼러 바 표시 X
            )
plt.show()



