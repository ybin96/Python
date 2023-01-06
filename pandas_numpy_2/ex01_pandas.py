import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./Data/scores.csv")
# print(df)
# print(type(df))
# a = df.loc[5]
# b = df.iloc[5]
# print(a)
# print(b)
df.index = df.name
# print(df)
del df['name']
print(df)
# print(df)
# df['music'] = 100
# print(df)

'''
<< 팀별 연습 문제 >>
1) 1반 학생의 이름,국어,수학만 출력 해 봅니다.
2) 1반 학생의 과목별 평균을 구해 봅니다.
3) 모든 학생에 대하여 평균컬럼을 추가 해 봅니다.
4) 성적이 높은 순으로 출력 해 봅니다.
'''
# 1) 1반 학생의 이름,국어,수학만 출력 해 봅니다.
class_1 = df[df['class']==1]
a= class_1[['kor','mat']]
print(a)

# 2) 1반 학생의 과목별 평균을 구해 봅니다.
print(class_1)
print('1반사람수',len(class_1))
subject = ['kor','eng','mat','bio']
# b = class_1[subject].sum()/len(class_1)
c= class_1[subject].sum(axis=0)/len(class_1)
c_1 = class_1[subject].mean(axis=0)
d = class_1[subject].sum(axis=1)/len(subject)
d_1 = class_1[subject].mean(axis=1)
# print(b)
print(c)
print(c_1)
print("-"*50)
print(d)
print(d_1)


# 3) 모든 학생에 대하여 평균컬럼을 추가 해 봅니다.
print('-'*50)
print(df)
df['avg'] = df[subject].mean(axis=1)
print(df)


# 4) 성적이 높은 순으로 출력 해 봅니다.
# sorted_df = df.sort_values('avg')     #오름차순정렬
sorted_df = df.sort_values('avg',ascending=False)
print(df)
print("-"*50)
print(sorted_df)

print("-"*50)
print(sorted_df.head())
print("-"*50)
print(sorted_df.head(1))
print("-"*50)
print(sorted_df.tail(1))
print('-'*50)

# sorted_df['avg'].plot(kind='bar')
# plt.show()

class_2 = df[df['class']==2]
class_1 = df[df['class']==1]

del class_1['class']
del class_2['class']

class_1.plot(kind='box')
class_2.plot(kind='box')
plt.show()



# a = df.loc['ben']
# b = df.iloc[2]              #시리즈를 반환합니다. (시리즈는 마치 자바의  map, 원래 파이썬의 dictionary 처럼 key,value가 한쌍으로 이루어짐)
# print(a)
# print(b)
# print(a.index)
# print(a.values)             #시리즈로 부터 값만 갖고 와요!



#연습) ben부터 paul까지의 데이터를 모두 출력 해 봅니다. loc, iloc      완성하면 "1"
# a = df.loc['ben':'paul']            # loc은 마지막 인덱스가 포함이 됩니다.
# print(a)
# b = df.iloc[2:6]                    # iloc은 마지막 인덱스가 포함되지 않아요!
# print(b)


#연습) 모든 학생의 class, kor, mat 만 출력 해 봅니다.             완성하면 "1"
# a = df[['class','kor','mat']]
# print(a)
# subject = ['class','eng','mat']
# a = df[subject]
# print(a)



#연습) 1반학생만 모두 출력 해 봅니다.
#연습) 2반학생만 모두 출력 해 봅니다.             완성하면 "1"
# a = df[df['class'] == 1]
# print(a)
#
# b = df[df['class'] == 2]
# print(b)


def pro1():
    df = pd.read_csv("./Data/scores.csv")
    print(df)
    #인덱스를 학생의 이름으로 변경 해 봅시다
    df.index = df.name

    #학생이름이 인덱스가 되었으니 컬럼에서는 삭제하도록 합니다.
    del df['name']
    print(df)

    #첫번째 학생  'adam'의 데이터를 출력 해 봅시다.
    # print(df['adam'])   #속성(칼럼)중에 adam를 찾아요
    print(df.loc['adam'])
    print(df.iloc[0])
    # print(df.iloc['adam'])             #오류        iloc에는 숫자 인덱스가 와야 합니다.
    # print(df.loc[0])                   #오류        문자인덱스가 설정되어있을때에는 문자인덱스가 와야 합니다.

    # a = df.iloc[0]
    # print(a)
    # print(type(a))





    # print(type(df))
    # print("index:",df.index)                #RangeIndex(start=0, stop=12, step=1)
    # print("columns:",df.columns)            #Index(['class', 'name', 'kor', 'eng', 'mat', 'bio'], dtype='object')
    # print('values:',df.values)              #행머리글, 열머리글을 제외한 값만 2차원배열로 갖고 옵니다.
    #
    # #이름만 출력 해 봅니다.
    # print(df['name'])
    # print(df.name)

    # name = df.name
    # print(name)
    # print(type(name))
