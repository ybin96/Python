import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titaic = sns.load_dataset('titanic')

#pairplot : 매개변수로 전될되는 변수의 리스트를 각각 행열로 한 만큼의 화면을 만들고
#                   두 변수가 격자로 만나는 지점에 두 변수간의 관계를 산점도를 그려 주고
#                   동일한 변수일때에는 히스토그램을 그려줍니다.

my_col = ['age','pclass','fare']

a = sns.pairplot(titaic[my_col])
plt.show()













