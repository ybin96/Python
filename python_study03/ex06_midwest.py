'''
1. midwest.csv를 불러와 데이터의 특징을 파악합니다
2. poptotal(전체인구) 변수를 total로, popasian(아시아 인구) 변수를 asian으로 수정합니다.
3. total, asian 변수를 이용해 '전체 인구 대비 아시아 인구 백분율' 파생변수를 추가하고
    히스토그램을 만들어 분포를 살펴 봅니다ㅣ
4. 아시아 인구 백분율 전체 평균을 구하고 평균을 초과하면 'large', 그렇지 않으면 'small'을
    부여한 파생변수를 만들어 봅니다.
5. 'large'와 'small'에 해당하는 지역이 얼마나 많은지 빈도표와 막대그래프를 만들어
    확인해 봅니다.
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("../Data/midwest.csv")
# print(df)
# 1. midwest.csv를 불러와 데이터의 특징을 파악합니다
# print(df.head(1))
# print(df.tail(1))
# print(df.shape)
# print(df.info())
# print(df.describe())

#2. poptotal(전체인구) 변수를 total로, popasian(아시아 인구) 변수를 asian으로 수정합니다.
df = df.rename(columns={'poptotal':'total','popasian':'asian'})
print(df.info())

# 3. total, asian 변수를 이용해 '전체 인구 대비 아시아 인구 백분율' 파생변수를 추가하고
#     히스토그램을 만들어 분포를 살펴 봅니다ㅣ

df['rate'] = df['asian'] / df['total'] * 100
print(df[['county','rate']])
# df['rate'].plot.hist()
# plt.show()

# 4. 아시아 인구 백분율 전체 평균을 구하고 평균을 초과하면 'large', 그렇지 않으면 'small'을
#     부여한 파생변수를 만들어 봅니다.

print(df['rate'].mean())    #0.4872461834357345
df['group'] = np.where(df['rate']>0.4872, 'large', 'small')
print(df.info())
print(df[['county','group']])

# 5. 'large'와 'small'에 해당하는 지역이 얼마나 많은지 빈도표와 막대그래프를 만들어
#     확인해 봅니다.
group_count = df['group'].value_counts()
print(group_count)

group_count.plot.bar(rot=0)
plt.show()




