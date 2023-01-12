import pandas as pd
import numpy as np

test1 = pd.DataFrame({
    'name':["홍길동","김길동","이순신","김순신","유관순","김관순","이관순"],
    'id':[1,2,3,4,5,6,7],
    'midterm':[60,80,70,90,85,100,90]
})

test2 = pd.DataFrame({
    'no':[1,2,3,4,5],
    'name':["홍길동","김길동","이순신","김순신","유관순"],
    'final':[70,83,65,95,80]
})


# how="left"        마치 sql의 left outter join 처럼 동작합니다.
# 이때에는 합쳐진 다른쪽에 데이터프레임에는 값이 존재하지 않기 때문에 결측치( NaN)가 생성됩니다.
test2 = test2.rename(columns={'no':'id'})
tot = pd.merge(test1, test2, how='left')
print(tot)
tot = tot[["id","midterm","final","name"]]
# 원하는 속성만 추출하는 표현이지만 컬럼의 순서를 바꿀때도 사용할 수 있어요
print(tot)
'''
   id  midterm  final
0   1       60   70.0
1   2       80   83.0
2   3       70   65.0
3   4       90   95.0
4   5       85   80.0
5   6      100    NaN
6   7       90    NaN
'''










