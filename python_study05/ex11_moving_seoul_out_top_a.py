import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("../Data/시도별 전출입 인구수.xlsx", header=0)
df = df.fillna(method='ffill')
print(df.shape)             #(325, 50)
df = df[df['전출지별'] == "서울특별시"]
df = df.loc[21:]
year_list = np.arange(2000,2011)
year_list = list(map(str, year_list))

df['total'] = df.loc[:,year_list].sum(axis=1)

df = df.rename(columns={'전입지별':'city'})
df = df[df['city'] != "세종특별자치시"]
print(df.loc[:,['city','total']])
# print(df)
#

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

sns.barplot(data=df, x='total', y='city')
plt.show()

# 한글설정
# !sudo apt-get install -y fonts-nanum
# !sudo fc-cache -fv
# !rm ~/.cache/matplotlib -rf
# plt.rc('font', family='NanumBarunGothic')
