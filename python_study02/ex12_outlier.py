import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mpg = pd.read_csv("../Data/mpg.csv")

#값의 분포를 확인 하기 위하여 "상자그림"를 그려 봅니다.
#상자그림을 그리면 극단치가 있는 확인 할 수 있어요
# sns.boxplot(data=mpg, y='hwy')
# plt.show()

#InterQuartile Range, 사분범위
#IQR = 3사분위값 - 1사분위값

#1사분위 : 값을 순서데로 놓았을때에 하위 25%값
#2사분위 : ~~                       50%값
#3사분위 : ~~                       75%값
#아래수염 : 0~25%
#윗수염 : 75~100%

#1사분위 값을 알아 봅시다.
pct25 = mpg['hwy'].quantile(.25)
print(pct25)#18.0

#3사분위 값을 알아 봅시다.
pct75 = mpg['hwy'].quantile(.75)
print(pct75)  #27.0

#사분범위(IQR)을 알아 봅시다.
iqr = pct75 - pct25
print(iqr)  #9.0

#극단치 경계값
#하한경계값      : 1사분위 - 사분범위 1.5
#상한경계값      : 3사분위 + 사분범위 1.5

limit_down = pct25 - iqr * 1.5
limit_up = pct75 + iqr * 1.5
print("극단치 하한 경계값:",limit_down)     #4.5
print("극단치 상한 경계값:",limit_up)       #40.5

#극단치 경계값을 알았으니 hwy가 이 범위를 넘으면 이상치로 보고 결측치 처리 합시다.
mpg['hwy'] = np.where( (mpg['hwy'] < 4.5) | (mpg['hwy'] > 40.5), pd.NA, mpg['hwy'])
# mpg['hwy'] = np.where(4.5 <= mpg['hwy'] <= 40.5, mpg['hwy'], pd.NA )        #오류
print(mpg['hwy'].isna().sum())  #3













