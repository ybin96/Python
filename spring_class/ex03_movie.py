import numpy as np
import pandas as pd


pd.set_option('display.max_columns',100)

#3개의 데이터파일을 읽어 들여 하나의 데이터프레임으로 반환하는 함수를 만들고 호출해 봅니다.  완성하면 "1"
def getMovies():
    users = pd.read_csv("./Data/users.dat",
                        sep="::",
                        engine='python',
                        header=None, names=['UserID','Gender','Age','Occupation','Zip-code'])

    movies = pd.read_csv("./Data/movies.dat",
                         sep="::",
                         engine='python',
                         header=None,
                         names=['MovieID','Title','Genres'])
    ratings = pd.read_csv('./Data/ratings.dat',
                           sep="::",
                           engine='python',
                           header=None,
                           names=['UserID','MovieID','Rating','Timestamp'])
    return pd.merge(pd.merge(ratings,users),movies)


def getOver500(df):
    df2 = df.groupby('Title').size()
    return df2[df2 >= 500].index

df = getMovies()
over500_index = getOver500(df)
print(over500_index)
#팀별연습문제) 여자가 더 좋아한는 영화 5개를 출력
#            남자가 더 좋아하는 영화 5개 출력


#성별별로 영화별로 평점의 평균을 출력
# print(df.head(1))
by_gender = df.pivot_table(values='Rating', columns='Gender', index='Title')
# print(by_gender)
print(len(by_gender))

rating_500 = by_gender.loc[over500_index]
# print(rating_500)
print(len(rating_500))
print(rating_500)
rating_500['Diff'] = rating_500['F'] - rating_500['M']
print(rating_500)

female_better = rating_500.sort_values(by='Diff', ascending=False)
print(female_better.head())
print(female_better.tail())

#            호불호가 갈리지 않는 영화 5개 출력
rating_500['Dist'] = ( rating_500['F'] - rating_500['M']  ).abs()
print(rating_500)

together = rating_500.sort_values(by='Dist')
print(together.head())


# a = df.pivot_table(values='Rating', index='Title')
# a = a.loc[over500_index]
# b = a.sort_values(by='Rating', ascending=False).head(5)
# print(b)

#연습) 평가회수가 500번 이상인 영화에 대하여 평점평균가 가장 높은 5개의 영화를 출력
#               완성하면 "3"





# print(df.head(1))

#연습) 데이터프레임을 매개변수로 전달받아 빈도수가 500번 이상인 영화제목을 반환하는 함수를 만들고 호출 해 봅니다.
#                   완성하면 "3"

#각 영화별로 레코드의 수(각 영화별 평가수를 출력)
# select Title, count(*) from group by Title
# df2 = df.groupby('Title').size()
# print(df2[df2>=500].index)
# print(df2 >= 500)
# print(type(df2))

#연습) 빈도수가 500이상인 영화제목을 출력 해 봅니다.        완성하면 "1"


# #평점평균이 가장 높은 5개의 영화제목을 출력                   완성하면 "3"
# a = df.pivot_table(values='Rating', index='Title')
# b = a.sort_values(by='Rating', ascending=False).head(5)
# print(b)
#
# r = df[df['Title'] == 'Ulysses (Ulisse) (1954)']
# print(len(r))           #1
# # 1명이 평가해서 5점을 주었어요,    이것은 신뢰할 수 없어요.
# # 가장 평점평균이 높은 영화 5개를 뽑고자 하는데
# #   평가횟수가 500번 이상인 영화를 대상으로 하고 싶어요!


# #연습) 나이별로 성별별로 별점의 총합을 출력 해 봅니다.
# # t9 = df.pivot_table(values='Rating', index='Gender', columns='Age', aggfunc='sum')
# # print(t9)
# #
# # t9_1 = df.pivot_table(values='Rating', columns='Gender', index='Age', aggfunc='sum')
# # print(t9_1)
#
#
# #연습) 나이별로 성별별로 별점의 평균과 총합을 출력 해 봅니다.                완성하면 "1"
# t10_1 = df.pivot_table(values="Rating", index='Age', columns="Gender", aggfunc="mean")
# t10_2 = df.pivot_table(values='Rating', index='Age', columns="Gender", aggfunc='sum')
# print(t10_1)
# print(t10_2)
# # a = pd.merge(t10_1, t10_2)
# # print('합친 데이터')
# # print(a)
# b = pd.concat([t10_1,t10_2])            #수직
# print(b)
# c = pd.concat([t10_1, t10_2], axis=1)   #수평
# print(c)
#
#
# t10 = df.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=["mean", "sum"])
# # t10 = df.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=[np.mean, np.sum])
# # # t10 = df.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc=["mean, sum"])
# print(t10)
#



# print(df[['Gender','Age','Rating']])    #성별별로 나이별로 별점의 평균
#
# t8 = df.pivot_table(values='Rating', index=['Gender', 'Age'])
# print(t8)
# #
# t8_1 = t8.unstack()         # index     --> column
# print(t8_1)
#
# t8_2 = t8_1.stack()         # column    --> index
# print(t8_2)



#연습) 성별별로 나이별로 직업별로 별점의 평균을 출력 해 봅니다.    완성하면 "3"
# t6 = df.pivot_table(values='Rating', index=['Gender','Age'], columns='Occupation')
# print(t6)

# t7 = df.pivot_table(values='Rating', index=['Gender','Age'], columns='Occupation', fill_value=0)
# print(t7)

# t5 = df.pivot_table(values='Rating', columns=['Gender','Age'])
# print(t5)

# t4 = df.pivot_table(values='Rating', index=['Gender','Age'])
# print(t4)


# t3 = df.pivot_table(values='Rating', index='Gender', columns='Age', aggfunc='mean')
# print(t3)
# print("-"*50)
# t3.columns = ["Under 18", "18-24","25-34","35-44","45-49","50-55","56+"]
# print(t3)

# t2 = df.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc='mean')
# print(t2)
#
# t2.index = ["Under 18", "18-24","25-34","35-44","45-49","50-55","56+"]
# print(t2)




#연습) 남자들의 별점평균과 여자들의 별점평균을 출력 해 봅니다.        완성하면 "3"
#연습) 성별별로 별점의 평균을 출력합니다.
# t1 = df.pivot_table(values="Rating", index="Gender")
# t2 = df.pivot_table(values='Rating', columns='Gender')
# print(t1)
# print(type(t1))
# print(t2)
# print(type(t2))

# df_m = df[df['Gender'] == 'M']
# df_w = df[df['Gender'] == 'F']
# print('남자.......................')
# print(df_m)
# print('여자.......................')
# print(df_w)
# print('남자의 평균',df_m['Rating'].mean())
# print('여자의 평균',df_w['Rating'].mean())