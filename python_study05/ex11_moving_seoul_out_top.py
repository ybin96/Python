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
# print(df)
df = df.loc[21:]
# print(df)
# a = []
# year_list = np.arange(2000,2011)
# for i in year_list:
#     a.append(str(i))
# print(a)
year_list = np.arange(2000,2011)
year_list = list(map(str, year_list))
print(year_list)

# print(df.loc[:,year_list].sum(axis=1))
df['total'] = df.loc[:,year_list].sum(axis=1)
print(df)

# print(type(year_list))
# year_list = ['2000', '2001', '2002']
# df  = df.loc[:,year_list].sum(axis=1)
# print(df)

# df['total'] = df['2000'] + df['2001']
# year_list = np.arange(2000,2011).tostring()

# print(df[year_list].sum())
# print(year_list)
# print(type(year_list))
# print(df)
