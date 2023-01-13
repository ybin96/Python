import pandas as pd
exam = pd.read_csv("../Data/exam.csv")
# print(exam)
# class1 = exam.query('nclass == 1')
# print(class1)
#
# class2 = exam.query('nclass == 2')
# print(class2)
#
# class_not1 = exam.query('nclass != 1')
# print(class_not1)
#
# class_not3 = exam.query('nclass != 3')
# print(class_not3)

# class1 = exam[ exam['nclass'] == 1]
# print(class1)

# df = exam.query('math > 50')
# print(df)

# df = exam.query('math < 50')
# print(df)

# df = exam.query('english >= 50')
# print(df)

# df = exam.query('english <= 80')
# print(df)

#1반이면서 수학점수가 50점 이상인 경우
# df = exam.query('nclass==1 & math >= 50')
# print(df)


#2반이면서 영어점수가 80점이상인 경우
# df = exam.query('nclass == 2 & english >= 80')
# print(df)

#수학,과학,영어 모두 60점 이상인 경우
# df = exam.query('math>=60 & science >= 60 & english >= 60')
# print(df)

#수학점수가 90점 이상이거나 영어점수가 90점 이상인 경우
# df = exam.query('math >= 90 | english >= 90')
# print(df)

#영어점수가 90점 미만이거나 과학점수가 50점미만인 경우
# df = exam.query('english < 90 | science < 50')
# print(df)

#1,3,5반에 해당하는 행 추출
# df = exam.query('nclass == 1 | nclass == 3 | nclass == 5')
# print(df)

# df = exam.query('nclass in [1,3,5]')
# print(df)

#1반과 2반중에 어느반이 수학을 잘 하는지?
nclass1 = exam.query('nclass == 1')
nclass2 = exam.query('nclass == 2')
print(nclass1)
print(nclass2)
print(nclass1['math'].mean())
print(nclass2['math'].mean())
# 46.25
# 61.25

df = exam.query('nclass==1 | nclass==2').pivot_table(values='math', aggfunc='mean', index='nclass')
print(df)

df = pd.DataFrame({
    'sex':['F','M','F','M'],
    'country':['Korea','China','Japan','USA']
})
print(df)

a = df.query('sex == "F" & country == "Korea"')
print(a)
b = df.query("sex == 'F' & country == 'Korea'")
print(b)
# c = df.query('sex == 'F' & country == 'Korea'') #X
# print(c)

var = 3
df = exam.query('nclass == @var')
print(df)

a = exam['math']
print(a)
print(type(a))

a = exam['english']
print(a)

a = exam[['nclass', 'math', 'english']]
print(a)
print(type(a))

arr = ['nclass', 'math', 'english']
a = exam[arr]
print(a)

a = exam['math']        #한개의 속성을 갖고 오면 시리즈입니다.
b = exam[['math']]      #한개이지만 이중 괄호로 갖고 오면 데이터프레임이 됩니다.
print(a)
print(b)
print(type(a))
print(type(b))

print(exam.info())

a = exam[['id','nclass','english','science']]
print(a)
b = exam.drop(columns='math')                    #수학빼고 다른 속성을 갖고 옵니다.
print(b)
print(exam)

c = exam.drop(columns=['math','english'])       #제외시킬 칼럼이 여러개일때 리스트로 묶어요
print(c)

# 행추출 query
# 열추출 []

#1반의 영어점수만 추출
a = exam.query('nclass == 1')['english']
print(a)

# b = exam[['english']].query('nclass==1')
# print(b)

#수학이 50이상인 행만 추출한 다음  id,  math 추출
# a = exam.query('math >= 50')[['id','math']]
# print(a)

# a = exam[['id','math']].query('math >= 50')
# print(a)

#math가 50이상인 행만 추출한 다음 id,math 앞부분 5개만 출력
a = exam.query('math >= 50')[['id','math']].head()
print(a)

a = exam.query('math >= 50')[['id','math']].head(10)
print(a)

#여러개의 명령어를 메소드 체이닝으로 작성할 때에 한줄에 하나의 명령어를 쓰면 가독성을 높일 수 있어요
#그때에 줄 끝에 \를 붙여요
#그 뒤에는 아무것도 올 수 없어요!
a = exam.query('math >= 50') \
    [['id','math']] \
    .head(10)
print(a)

df = exam.sort_values(['math'])
print(df)
print(exam)

df  = exam.sort_values('math', ascending=False)
print(df)

df  = exam.sort_values(['nclass','math'])
print(df)

df = exam.sort_values(['nclass','math'], ascending=[True,False])
print(df)

df1 = exam.copy()
df1['total'] = df1['math'] +  df1['english'] +  df1['science']
df2 = exam.assign(total = exam['math'] + exam['english'] + exam['science'])

print(df1)
print(df2)








