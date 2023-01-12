import pandas as pd
import numpy as np

exam = pd.read_csv("../Data/exam.csv")
print(exam)
exam.loc[[2,7,14],['math']] = np.nan
print(exam)
print(exam['math'].mean())  #55.23529411764706

print('수학의 결측치 수 ==>',exam['math'].isna().sum())
# exam['math'] = exam['math'].fillna(55)
# print(exam)

exam['math'] = exam['math'].fillna(  int(exam['math'].mean())  )
print(exam)
print('수학의 결측치 수 ==>',exam['math'].isna().sum())