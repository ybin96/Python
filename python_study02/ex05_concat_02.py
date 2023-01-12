import pandas as pd
import numpy as np

group_a = pd.DataFrame({
    'id':[1,2,3,4,5],
    'name':["김유신","이유신","박유신","홍유신","최유신"],
    'test':[60,70,80,90,85]
})

group_a = group_a[['id','test']]

group_b = pd.DataFrame({
    'id':[6,7,8,9,10],
    'test':[70,83,65,95,80]
})

print(group_a)
print(group_b)

group_all = pd.concat([group_a,group_b])
print(group_all)

'''
id name  test
0   1  김유신    60
1   2  이유신    70
2   3  박유신    80
3   4  홍유신    90
4   5  최유신    85
0   6  NaN    70
1   7  NaN    83
2   8  NaN    65
3   9  NaN    95
4  10  NaN    80

세로로 합칠때에 두개의 데이터프레임의 속성의 수가 다르면
    그만큼 NaN이 생깁니다.
'''













