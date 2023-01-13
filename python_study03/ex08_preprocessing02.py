import numpy as np
import pandas as  pd

exam = pd.read_csv("../Data/exam.csv")
# print(exam)
#
# #원래의 데이터프레임인 exam에서는 변동이 없고  변수(속성)를 추가한 새로운 데이터프레임을 반환합니다.
# df1= exam.assign(total = exam['math'] + exam['english'] + exam['science'])
# print(df1)
# print(exam)
#
# df2 = exam.assign(total = exam['math'] + exam['english']+exam['science'],
#                   mean=(exam['math'] + exam['english']+exam['science'])/3)
# print(df2)
#
# df3 = exam.assign(test = np.where(exam['science'] >= 60, 'pass','fail'))
# print(df3)
#
# # assing함수로 추가한 파생변수를 메소드 체이닝으로 연결된 함수에서 그 변수를 바로 활용할 수 있어요!
# df4 = exam.assign(total = exam['math'] + exam['english'] + exam['science'])\
#     .sort_values('total',ascending=False)
# print(df4)

#

# # def pro(a):
# #     return a['math'] + a['english'] + a['science']
#
# pro = lambda a:a['math'] + a['english'] + a['science']
#
# #람다함수를 이용하면 긴 데이터프레임이름을 줄여서 사용할 수 있어요.
# # df4 = exam.assign(total = lambda a:a['math'] + a['english'] + a['science'])\
# #     .sort_values('total',ascending=False)
# # print(df4)
#
#
# # df4 = exam.assign(total = pro(exam))\
# #     .sort_values('total',ascending=False)
# # print(df4)
#
# # df5 = exam.assign(total = lambda x:x['math']+x['english']+x['science'])\
# #     .sort_values('total', ascending=False)
# # print(df5)
#
# #원래 데이터프레임이름과 람다식을 섞어서 쓸 수도 있어요
# df6 = exam.assign(total = exam['math'] + exam['english'] + exam['science'],
#                   mean = lambda a:a['total']/3)
# print(df6)

#오류
#assign함수로 한번에 여러개의 파생변수를 만들때에
#앞에서 변수가 람다식이 아닌 일반식으로 만든 변수일때에 일반식으로는 바로 사용할 수 없어요.
#람다식으로는 참조할 수 있어요.
# df6 = exam.assign(total = exam['math'] + exam['english'] + exam['science'],
#                   mean = exam['total']/3)
# print(df6)

#
# df7 = exam.assign(total = lambda a:a['math'] + a['english']+ a['science'],
#                   mean = lambda a:a['total']/3)
# print(df7)
#
#

# 수학에 대한 평균 구하기
df = exam.agg(mean_math = ('math','mean'))
print(df)
print(type(df))
#             math
# mean_math  57.45
# <class 'pandas.core.frame.DataFrame'>

a = exam['math'].mean()
print(a)
print(type(a))
# 57.45
# <class 'numpy.float64'>

#agg함수는 단독으로 쓰이는 경우는 별로 없어요
#group by와 같이 사용합니다.
#반별로 수학의 평균을 알아 봅시다.
df = exam.groupby('nclass', as_index=False)\
    .agg(mean_math=('math','mean'))
print(df)
print(type(df))

# df2 = exam.pivot_table(values='math', index='nclass', aggfunc='mean')
# print(df2)
# print(type(df2))

df2  = exam.groupby('nclass')\
    .agg(mean_math = ('math','mean'),
         sum_math=('math','sum'),
         median=('math','median'),
         n = ('math','count'))
print(df2)

df3 = exam.groupby('nclass').mean()
print(df3)





