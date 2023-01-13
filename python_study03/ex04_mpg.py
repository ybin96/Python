import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mpg = pd.read_csv('../Data/mpg.csv')
print(mpg)
mpg['total'] = (mpg['cty'] + mpg['hwy'])/2
print(mpg.head())
print(sum(mpg['total'])/len(mpg))   #20.14957264957265
print(mpg['total'].mean())          #20.14957264957265
print(mpg['total'].describe())
# count    234.000000
# mean      20.149573
# std        5.050290
# min       10.500000
# 25%       15.500000
# 50%       20.500000               <--- 중앙값
# 75%       23.500000
# max       39.500000
# mpg['total'].plot.hist()
# plt.show()

mpg['test'] = np.where(mpg['total'] >= 20, 'pass','fail')
print(mpg.head())
print(mpg.tail())

#test속성의 값의 종류별로 개수를 알려 줍니다.
count_test = mpg['test'].value_counts()
print(count_test)
# pass    128
# fail    106

# count_test.plot.bar(rot=0)
# plt.show()

mpg['grade'] =  np.where(mpg['total']>=30, "A",
                np.where(mpg['total']>=20,"B","C"))

print(mpg.head())

# count_grade = mpg['grade'].value_counts()
# count_grade = mpg['grade'].value_counts().sort_index()
# print(count_grade)
# print(type(count_grade))
# count_grade.plot.bar(rot=0)
# plt.show()

# df = mpg['grade']
# # print(df)
# # print(type(df))
# df = df.value_counts()
# # print(df)
# # print(type(df))
# df = df.sort_index()
# print(df)
# print(type(df))

# df = mpg['grade'].value_counts().sort_index()
# print(df)
# print(type(df))

mpg['grade2'] = np.where(mpg['total']>=30,"A",
                np.where(mpg['total']>=25,"B",
                np.where(mpg['total']>=20,"C","D")))

count_grade2 = mpg['grade2'].value_counts()
print(count_grade2)
# count_grade2.plot.bar(rot=0)
# plt.show()

print(mpg['category'].value_counts())

# mpg['size'] = np.where((mpg['category']=='compact')|
#                        (mpg['category']=='subcompact')|
#                        (mpg['category']=='2seater'),
#                        'small','large')

small = ['compact','subcompact','2seater']
mpg['size'] = np.where(mpg['category'].isin(small),'small','large')

print(mpg)
print(mpg['size'].value_counts())








