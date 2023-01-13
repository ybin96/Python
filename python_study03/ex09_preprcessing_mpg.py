import pandas as pd
mpg = pd.read_csv("../Data/mpg.csv")
print(mpg)

#제조사별로, 구동방식별로 도시연비의 평균
df = mpg.groupby(['manufacturer','drv'])\
    .agg(mean_cty = ('cty','mean'))
print(df)

#audi의 drv별로 빈도수를 출력
df2 = mpg.query('manufacturer == "audi"')\
    .groupby('drv')\
    .agg(n=('drv','count'))
print(df2)

df3 = mpg.groupby('drv')\
    .agg(n=('drv','count'))

print(df3)
print(type(df3))
print(df3.info())

df4 = mpg['drv'].value_counts()
print(df4)
print(type(df4))
print(df4.query('n>=100'))
# AttributeError: 'Series' object has no attribute 'query'












