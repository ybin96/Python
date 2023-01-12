import pandas as pd
import numpy as np

df = pd.DataFrame({
    'sex':[1,2,1,3,2,1],
    'score':[5,4,3,4,2,6]
})

print(df)
#이상치를 파악하기 위하여 값의 종류별 빈도수를 구합니다.
# print(df['sex'].value_counts())
# # 1    3
# # 2    2
# # 3    1            <------   성별의 종류로 나올 수 없는 값이 있어요  ==> 이상치
#
# print(df['score'].value_counts())
# 4    2
# 5    1
# 3    1
# 2    1
# 6    1           <----        score의 정상범위 1~5가 아닌 6이 있어요      ==> 이상치

# 이상치가 있으면
#   그것을 결측치로 처리 합니다.
# 성별에 대하여 이상치를 확인 해 보니 이상한 값 3이 있어요. 이것을 결측치로 처리 해 봅니다.
# df['sex'] = np.where(df['sex'] == 3, np.nan, df['sex'])
df['sex'] = np.where(df['sex'] == 3, pd.NA, df['sex'])
print(df)
'''
   sex  score
0  1.0      5
1  2.0      4
2  1.0      3
3  NaN      4
4  2.0      2
5  1.0      6
'''
# 성별의 자료형의 실수가 되었어요             <-----------------

# score에 대해서도 5보다 크다면 NaN을 설정합니다.
# df['score'] = np.where(df['score'] > 5, np.nan, df['score'])
# print(df)

df['score'] = np.where(df['score'] > 5, pd.NA, df['score'])
print(df)

# df = df.dropna(subset=['score','sex'])
# print(df)

# df['sex'] = pd.to_numeric(df['sex'], downcast='integer')
# df['score'] = pd.to_numeric(df['score'], downcast='integer')
# df['sex'] = df['sex'].astype(int)
# df['score'] = df['score'].astype(int)
# print(df)

print(df.dropna(subset=['sex','score'])\
    .groupby('sex')\
    .agg(mean_score = ('score','mean')))












