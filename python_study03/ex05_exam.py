import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("../Data/exam.csv")
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

df  = df.rename(columns={'english':'eng','science':'sci', 'math':'mat'})
print(df)
df['tot'] = df['mat'] + df['eng'] +  df['sci']
df['avg'] =  df['tot']//3
print(df)

#각 반별 인원수를 판별
class_count = df['nclass'].value_counts()
print(class_count)

#평균이 60점 이상이면 "합격", 그렇지 않으면 "불합격" 파생변수를 만들어 봅니다.
df['test'] = np.where(df['avg'] >= 60, "합격", "불합격")
print(df)
df['grade'] = np.where(df['avg']>=90,"A",
              np.where(df['avg']>=80,"B",
              np.where(df['avg']>=70,"C",
              np.where(df['avg']>=60,"D","F"))))
print(df)
grade_count = df['grade'].value_counts()
print(grade_count)
grade_count.plot.bar(rot=0)
plt.show()