import pandas as pd
import numpy as np

test1 = pd.DataFrame({
    'id':[1,2,3,4,5],
    'midterm':[60,80,70,90,85]
})

test2 = pd.DataFrame({
    'no':[1,2,3,4,5],
    'final':[70,83,65,95,80]
})

#만약에 합치고자 하는 두개의 데이터프레임의 컬럼이름이 다르다면
#동일하게 이름을 변경한 후에 merge를 해야합니다.
test2 = test2.rename(columns={'no':'id'})

print(test1)
print(test2)

total = pd.merge(test1, test2)      #똑같은 속성이 있으면 on를 생략할 수 있어요
print(total)












