import pandas as  pd
import numpy as np

'''연습) mpg데이터를 읽어 들여 다음을 실습 해 봅니다.         완성하면 "1"

연료종류별  가격
c  CNC              2.35
d  diesel           2.38
e  ethanol E85      2.11
p  premium          2.76
r  regular          2.22
'''
mpg = pd.read_csv("../Data/mpg.csv")
# print(mpg.info())
# print(mpg['fl'].value_counts())

# 1) 위의 내용에 따른 연료종류별 가격의 정보를 데이터프레임으로 만들어 봅니다.
df = pd.DataFrame({
    'fl':['c','d','e','p','r'],
    'price_fl':[2.35,2.38,2.11,2.76,2.22]
})
print(df)

# 2) mpg 데이터에는 연료 종류를 나타낸 f1변수는 있지만 연료가격을 나타낸 변수는 없습니다.
#         앞에서 만든 데이터를 이용하여 mpg데이터에 연료가격(price_fl) 변수를 추가합니다.

mpg = pd.merge(mpg, df)


# 3) 연료가격 변수가 잘 추가가 되었는지 확인하기 위하여 model,fl,price_fl 변수를
#         추출해 앞부분 5행을 출력 해 봅니다.
print(mpg[['model','fl','price_fl']].head())
print(mpg)
