import pandas as pd
import numpy as np

df = pd.DataFrame({
    'sex':['M','F',np.nan, 'M','F'],
    'score':[5,4,3,4,np.nan]
})

print(df)
print(df['score']+ 1)           #NaN에 어떤 연산을 하더라도 그 결과는 NaN입니다.

#대부분의 수집한 데이터는 결측치가 있기 마련입니다. 따라서  분석하기에 앞서 결측치가 있는지 파악하여
#결측치를 제거하거나
#다른 값으로 대체 한 후에 분석을 해야 합니다.   (평균,최빈값,...)

#결측치가 있는 확인 하기      isna
print(pd.isna(df))
#      sex  score
# 0  False  False
# 1  False  False
# 2   True  False
# 3  False  False
# 4  False   True

#실제로 수집한 데이터는 아주 많은 행과 아주 많을 열로 구성이 되어있어서
#위와 같은 방법으로 결측치가 있는지 파악하기는 어려워요

#각 속성별로 결측치가 몇개씩 있는지 알고 싶어요
print(pd.isna(df).sum())
# sex      1
# score    1
# dtype: int64

#수집한 데이터에 결측치가 있다면
#삭제 하거나 다른 값으로 대체합니다.

#score 컬럼에 결측치가 있는 행을 삭제합니다.
# df = df.dropna(subset=['score'])
# print(df)
# print(df['score'] + 1)

# df = df.dropna()              # <--- 결측치가 있는 행을 모두 삭제
# print(df)

#  성별,급여,주소
#       <--- 만약 성별별로 급여의 차이를 분석하고자 한다면
#               주소가 결측치 있어도 관계가 없어요!

# df = df.dropna(subset=['sex','score'])
# print(df)

print(df)
print(df['score']+ 1)           #NaN에 어떤 연산을 하더라도 그 결과는 NaN입니다.

#다음의 통계함수들은 결측치를 제거하고 수행합니다.
print(df['score'].mean())       #결측치를 제거하고 평균을 구해 줍니다.
print(df['score'].sum())

print(df.groupby('sex')\
    .agg(mean_score=('score','mean'),
         sum_score=('score','sum')))
