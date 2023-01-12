# midwest.csv는 미국 동부 지역의 인구통계 정보를 담고 있습니다. 이 파일을 읽어 들여 다음을 실습해 봅니다.
# 완성하면 "3"

import pandas as pd
import numpy as np

midwest = pd.read_csv('../Data/midwest.csv')
# print(midwest)
print(midwest.info())

# 1) popadults는 해당지역의 성인인구, poptotal은 전체인구를 나타냅니다.
# 	midwest데이터에 '전체인구 대비 미성년 인구 백분율' 변수를 추가 해 봅니다.
midwest['child_rate'] = (midwest['poptotal'] - midwest['popadults']) / midwest['poptotal'] * 100
print(midwest.head())

# 2) 미성년 인구 백분율이 가장 높은 상위 5개 country의 미성년 인구 백분율을 출력 합니다.
print(midwest.sort_values(by='child_rate', ascending=False).head()[['county','child_rate']])

# 3) 다음 분류에 따라 미성년 인구 비율 등급 변수를 추가하고 각 등급에 몇개의
# 	지역이 있는지 알아 봅니다.
#
# 	40%이상	large
# 	30~40%	middle
# 	30%미만	small
midwest = midwest.assign(child_grade = np.where( midwest['child_rate'] >= 40, 'large',
                             np.where(midwest['child_rate'] >= 30, 'middle','small')))
print(midwest.head())
print(midwest['child_grade'].value_counts())
# middle    396
# large      32
# small       9

# 4) popasian은 해당지역의 아시아인 인구를 나타냅니다. '전체 인구 대비 아시아인 인구 백분율'
# 변수를 추가하고 하위 10개 지역의 state(주), country(지역), 아시아인 인구 백분율을 출력 합니다.
print(midwest.assign(asian_rate= midwest['popasian'] / midwest['poptotal'] * 100)\
    .sort_values(by='asian_rate')\
    .head(10)[['state','county','asian_rate']])

