'''팀별연습문제 ) mpg.csv를 읽어 들여 다음을 실습 해 봅니다.

1. 자동차 배기량에 따라 고속도로 연비가 다른지 알아보려고 합니다. displ(배기량)이 4
이하인 자동차와 5이상인 자동차 중 어떤 자동차의 hwp(고속도로 연비) 평균이 더 높은지 알아 봅니다.

2. 자동차 제조 회사에 따라 도시 연비가 어떻게 다른지 알아보려고 합니다. 'audi'와 'toyota'중
어느 manufacturer(자동차 제조 회사)의 cty(도시 연비) 평균이 더 높은 알아 봅니다.

3. 'chevrolet', 'ford', 'honda' 자동차의 고속도로 연비 평균을 알아보려고 합니다. 세 회사의 데이터를
추출한 다음 hwy의 전체 평균을 구해봅니다.

4. mpg는 11개의 변수로 구성됩니다. 이 중 일부만 추출해 분석에 활용하려고 합니다. mpg 데이터에서
category(자동차 종류), cty(도시연비) 변수를 추출해 새로운 데이터를 만들어 봅니다.

5. 자동차 종류에 따라 도시 연비가 어떻게 다른지 알아보려고 합니다. 앞에서 추출한 데이터를 이용하여
category(자동차 종류)가 'suv'인 자동차와 'compact'인 자동차 중 어떤 자동차의 cty(도시연비)
평균이 더 높은지 알아봅니다.

6. mpg 복사본을 만들고 cty와 hwy를 더한 합산 연비 변수를 추가합니다.

7. 앞에서 만든 합산연비 변수를 2로 나눠 "평균 연비 변수"를 추가 합니다.

8. 평균연비변수가 가장 높은 자동차 3종을 출력합니다.

9. 6~8번을 하나로 연결된 pandas 구문으로 만들어 봅니다.

10. mpg데이터의 catetory는 자동차를 특징에 따라 suv, compact등 일곱 종류로 분류합니다.
어떤 차종의 도시연비가 높은지 비교하기 위하여 catetory별 cty의 평균을 구해 봅니다.

11. 6번 문제에서 어떤 차종의 도시연비가 높은지 cty평균이 높은순으로 정렬하여 출력 해 봅니다.

12. 고속도로 연비가 가장 높은 회사 세곳을 출력합니다.

13. 어떤 회사에서 compact 차종을 가장 많이 생산하는지 알아 봅니다.'''

import pandas as pd
import numpy as np

#mpg.csv를 읽어 들여 다음을 실습 해 봅니다.
mpg = pd.read_csv("../Data/mpg.csv")

# 10. mpg데이터의 category는 자동차를 특징에 따라 suv, compact등 일곱 종류로 분류합니다.
# 어떤 차종의 도시연비가 높은지 비교하기 위하여 catetory별 cty의 평균을 구해 봅니다.
# df = mpg.pivot_table(values='cty', index='category')
df = mpg.groupby('category')\
    .agg(mean=("cty","mean"))
# print(df)
#                   cty
# category
# 2seater     15.400000
# compact     20.127660
# midsize     18.756098
# minivan     15.818182
# pickup      13.000000
# subcompact  20.371429
# suv         13.500000


# 11. 10번 문제에서 어떤 차종의 도시연비가 높은지 cty평균이 높은순으로 정렬하여 출력 해 봅니다.
df = df.sort_values(by='mean',ascending=False)
print(df)

# 12. 고속도로 연비가 가장 높은 회사 세곳을 출력합니다.
# print(mpg.info())
print(list(mpg.groupby('manufacturer')\
    .agg(mean=("hwy","mean"))\
    .sort_values(by="mean",ascending=False)\
    .head(3).index))

# 13. 어떤 회사에서 compact 차종을 가장 많이 생산하는지 알아 봅니다.'''
# print(mpg.info())
print(mpg.query('category == "compact"')\
    .groupby('manufacturer')\
    .agg(n=("manufacturer","count"))\
    .sort_values(by="n",ascending=False))



# # 6. mpg 복사본을 만들고 cty와 hwy를 더한 합산 연비 변수를 추가합니다.
# df = mpg.copy()
# # df['tot'] =  (df['cty'] + df['hwy'])/2
# df = df.assign(tot=df['cty'] + df['hwy'])
# print(df)
#
# # 7. 앞에서 만든 합산연비 변수를 2로 나눠 "평균 연비 변수"를 추가 합니다.
# df = df.assign(mean=df["tot"]/2)
# print(df)
#
# # 8. 평균연비변수가 가장 높은 자동차 3종을 출력합니다.
# print(df.sort_values(by='mean').tail(3))
#
# # 9. 6~8번을 하나로 연결된 pandas 구문으로 만들어 봅니다.
# print(mpg.copy()\
#     .assign(tot=mpg['cty']+mpg['hwy'], mean=(mpg['cty']+mpg['hwy'])/2)\
#     .sort_values(by='mean').tail(3))
#


# 4. mpg는 11개의 변수로 구성됩니다. 이 중 일부만 추출해 분석에 활용하려고 합니다. mpg 데이터에서
# category(자동차 종류), cty(도시연비) 변수를 추출해 새로운 데이터를 만들어 봅니다.

# df = mpg[['category','cty']]
# print(df)

# 5. 자동차 종류에 따라 도시 연비가 어떻게 다른지 알아보려고 합니다. 앞에서 추출한 데이터를 이용하여
# category(자동차 종류)가 'suv'인 자동차와 'compact'인 자동차 중 어떤 자동차의 cty(도시연비)
# 평균이 더 높은지 알아봅니다.

# print(df['category'].value_counts())
# df1 = df.query('category == "suv"')['cty'].mean()
# df2 = df.query('category == "compact"')['cty'].mean()
# print(df1, df2)     #13.5 20.127659574468087



# 3. 'chevrolet', 'ford', 'honda' 자동차의 고속도로 연비 평균을 알아보려고 합니다. 세 회사의 데이터를
# 추출한 다음 hwy의 전체 평균을 구해봅니다.
# df = mpg.query('manufacturer in ["chevrolet","ford","honda"]')['hwy'].mean()
# df1 = mpg[mpg['manufacturer'] == "chevrolet"]['hwy']
# df2 = mpg[mpg['manufacturer'] == "ford"]['hwy']
# df3 = mpg[mpg['manufacturer'] == "honda"]['hwy']
# df = pd.concat([df1, df2,df3]).mean()
# print(df)
# 22.50943396226415


# 2. 자동차 제조 회사에 따라 도시 연비가 어떻게 다른지 알아보려고 합니다. 'audi'와 'toyota'중
# 어느 manufacturer(자동차 제조 회사)의 cty(도시 연비) 평균이 더 높은 알아 봅니다.

# print( set(mpg['manufacturer']))
# a = mpg['manufacturer'].value_counts()
# print(a)

# df = mpg.query('manufacturer in ["audi","toyota"]')\
#     .pivot_table(values='cty',index='manufacturer')
# df = mpg.query('manufacturer in ["audi","toyota"]')\
#     .groupby('manufacturer')\
#     .agg(mean_cty=("cty","mean"))
# print(df)

# df1 = mpg.query('manufacturer == "audi"')['cty'].mean()
# df2 = mpg.query('manufacturer == "toyota"')['cty'].mean()
# # df1 = mpg[mpg['manufacturer'] == 'audi']['cty'].mean()
# # df2 = mpg[mpg['manufacturer'] == 'toyota']['cty'].mean()
# print(df1, df2) #17.61111111111111 18.529411764705884






#
# 1. 자동차 배기량에 따라 고속도로 연비가 다른지 알아보려고 합니다. displ(배기량)이 4
# 이하인 자동차와 5이상인 자동차 중 어떤 자동차의 hwp(고속도로 연비) 평균이 더 높은지 알아 봅니다.


# print(mpg)
# print(mpg.info())
# print(mpg['displ'])
# print(mpg['displ'].max())
# print(mpg['displ'].min())

# df1 = mpg[ mpg['displ'] <= 4]
# df2 = mpg[mpg['displ'] >= 5]
# df1 = mpg.query('displ <= 4')['hwy'].mean()
# df2 = mpg.query('displ >= 5 ')['hwy'].mean()
# print(df1,df2)      #25.96319018404908 18.07894736842105
# print(len(df1))
# print(len(df2))
# print(len(mpg))
# 163
# 38
# 234














