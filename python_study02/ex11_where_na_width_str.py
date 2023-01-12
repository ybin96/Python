import pandas as pd
import numpy as np

#이상치를 결측치로 치환하거나 파생변수를 만들때에 결측치를 설정하기 위하여
#   np.nan  정수=> 실수, 문자값을 같이 설정 X
#   pd.NA를 설정하여 문제를 해결 O

df = pd.DataFrame({
    'x1':[1,1,2,2]
})


#x1의 값에 따라서 1이면 'a', 그렇지 않으면  NaN을 갖는 속성  x2를 추가 합니다.
# df['x2'] = np.where(df['x1'] == 1, 'a', pd.NA)
# print(df)
# #    x1    x2
# # 0   1     a
# # 1   1     a
# # 2   2  <NA>
# # 3   2  <NA>
# print(df.isna().sum())
# x1    0
# x2    2


# df['x2'] = np.where(df['x1'] ==  '1', 'a', np.nan )
# print(df)
# print(df.isna().sum())
#    x1   x2
# 0   1  nan        <---- NaN(결측치)가 아니라 "nan"글자를 만들어 버려요.
# 1   1  nan
# 2   2  nan
# 3   2  nan
# x1    0       
# x2    0           <---- 기대하는 것은 NaN가 2개 나와야 되는데 0으로 나와요


df['x2'] = np.where(df['x1'] ==  1, 'a', np.nan )
df['x2'] = df['x2'].replace('nan',np.nan)
print(df)
print(df.isna().sum())

#    x1   x2
# 0   1    a
# 1   1    a
# 2   2  NaN
# 3   2  NaN
# x1    0
# x2    2
# dtype: int64




