import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("../Data/시도별 전출입 인구수.xlsx", header=0)
# print(df)

#셀이 병합이 되어 있어 NaN이 많아요
#이 경우 바로 앞의 값으로 채우면 될것 같아요          bfill : 바로 다음값과 동일하게
df = df.fillna(method='ffill')
# print(df)

# print(df.head())
print(df.shape)             #(325, 50)
# print(df.info())

df = df[df['전출지별'] == "서울특별시"]
df = df[df['전입지별'] == '경기도']
# print(df)
df = df.transpose()
# print(df)
# print(df.info())
print(type(df))
print(df.shape)
print(df.index)
df = df.iloc[2:]
print(df.index)
df.columns=["n"]
print(df)

sns.lineplot(data=df, x=  pd.to_datetime(df.index)  , y="n")
plt.show()


#연습) 연도별로 서울에서 경기도로 전출한 가구수의 변화를 그래프로 나타내 봅니다.
#                   완성하면 "1"

#   전출지별   전입지별      1970      1971  ...      2014      2015      2016      2017
# 0  전출지별   전입지별  이동자수 (명)  이동자수 (명)  ...  이동자수 (명)  이동자수 (명)  이동자수 (명)  이동자수 (명)
# 1    전국     전국   4046536   4210164  ...   7629098   7755286   7378430   7154226
# 2    전국  서울특별시   1742813   1671705  ...   1573594   1589431   1515602   1472937
# 3    전국  부산광역시    448577    389797  ...    485710    507031    459015    439073
# 4    전국  대구광역시         -         -  ...    350213    351424    328228    321182

#연습) 2000~2010사이에 서울에서 어느지역으로 전출을 가장 많이 했는지 파악하기 위한
#               그래프를 그려 봅니다.












