import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

#FacitGrid
#x,y의 값의 종류별로 화면을 분할하여 어떤 함수를 적용하여 그래프를 그리고자할 때에 사용합니다.

# x:who, row:survived 로 화면을 분할 합니다.
a = sns.FacetGrid(data=titanic, col='who', row='survived')   #6개의 화며으로 분할

#각화면에 나이의 히스토그램을 그려 보도록 합시다.
a = a.map( plt.hist, "age" )

plt.show()

