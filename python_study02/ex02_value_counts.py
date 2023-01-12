import pandas as  pd
import numpy as np

mpg = pd.read_csv("../Data/mpg.csv")
a = mpg['drv'].value_counts()
print(a)
print(type(a))          #<class 'pandas.core.series.Series'>

# b = mpg['drv'].value_counts().query("n>100")        #'Series' object has no attribute 'query'
# print(b)

# 값의 종류별 빈도수를 구하면 그것의 자료형은 시리즈 입니다. 그 상태에서는 조건에 맞는 데이터만 추출하기 위한
#   query 함수를 사용할 수 없고
#   to_frame 함수로 데이터프레임으로 변경한 후에 query를 사용할 수 있어요!
# a= mpg['drv'].value_counts()\
#     .to_frame('n')\
#     .rename_axis('drv')\
#     .query('n>100')
#
# print(a)
# print(type(a))

#연습) suv차종의 통합연비가 높은 5개의 제조사를 출력
# a = mpg.query('category == "suv"')
# print(len(mpg))       #234
# print(len(a))         #62


# print(mpg.info())

# a= mpg.query('category == "suv"')\
#     .assign(tot=(mpg["hwy"]+mpg["cty"])/2)\
#     .groupby('manufacturer')\
#     .agg(mean=("tot","mean"))\

# print(len(a))       #10
#
# print(len(set(mpg['manufacturer'])))        #15
#suv를 생산하지 않는 회사도 있을 수 있어요!

print(mpg.query('category == "suv"')\
    .assign(tot=(mpg["hwy"]+mpg["cty"])/2)\
    .groupby('manufacturer')\
    .agg(mean=("tot","mean"))\
    .sort_values(by="mean", ascending=False)\
    .head())

# subaru        21.916667
# toyota        16.312500
# nissan        15.875000
# mercury       15.625000
# jeep          15.562500





