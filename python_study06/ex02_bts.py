import pandas as pd
import numpy as np
import konlpy
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("../Data/news_comment_BTS.csv", encoding="UTF-8")
# print(df)
# print(df.info())
# reg_time reply press title url
# print(df['reg_time'])
# print(df['reply'])
# print(df['press'])
# print(df['title'])

print(df['reply'].head())
print("-"*50)
#reply에 한글을 제외한 모든 문제를 공백으로 처리합니다.
df['reply'] =  df['reply'].str.replace("[^가-힣]", " ", regex=True)

# 불용어에 대한 처리
stop_word = ["방탄","소년단","방탄소년단","가수"]
for w in stop_word:
    df['reply'] = df['reply'].str.replace(w, " ")


#동의어에 대한 처리
#원래글자 배열
old_word = [" 면제","군대","선양","국위","나라","대한","민국","한국","대박","진짜"]

#바꿀글자 배열
new_word = [" 군면제","군면제","국위선양","국위선양","대한민국","대한민국","대한민국","대한민국","최고","최고"]

for i in range(len(old_word)):
    df['reply'] = df['reply'].str.replace(old_word[i], new_word[i])

print(df['reply'].head())


# 대통령연설문이나 뉴스기사는 국어 문법을 잘 지킵니다.
#       이러한 문자열의 처리는 Hannanum을 이용합니다.
# 그러나 일반 사람들이 작성하는 뉴스의 댓글등 sns의 데이터들은 국어문법이 잘 지켜지지 않는 경우가 많아요
#       이러한 문자열의 처리는 Kkma를 이용합니다.

import konlpy
kkma = konlpy.tag.Kkma()

nouns = df['reply'].apply(kkma.nouns)
print(df['reply'])
print("-"*50)
print(nouns)
# 0                                        [국보, 국보소년단, 소년단]
# 1                                                   [아줌마]
# 2                   [팩트, 팩트체크, 체크, 보드, 위, 방탄, 방탄소년단, 소년단]
# 3              [방탄, 방탄소년단, 소년단, 한국, 한국사람, 사람, 자랑, 우리, 하자]
# 4                                       [월드, 클래스, 소식, 응원]

#출력을 해 보니 한 줄에 여러개의 단어가 들어 있어요
#한줄에 하나의 단어씩 들어가도록 만들어요.            explode()함수 이용
print(type(nouns))  #<class 'pandas.core.series.Series'>

nouns = nouns.explode()
print(nouns)

# 0          국보
# 0       국보소년단
# 0         소년단
# 1         아줌마
# 2          팩트

#한줄에 하나의 단어씩 들어가도록 만들었습니다.

#이것을 데이터프레임으로 만덜어 봅시다.
df_word = pd.DataFrame({'word':nouns})
print(df_word)

#       word
# 0        국보
# 0     국보소년단
# 0       소년단
# 1       아줌마
# 2        팩트

#위의 데이터프레임의 각 단어의 글자수를 구해서 변수(속성)를 추가합니다.
df_word['count'] = df_word['word'].str.len()
print(df_word)

#        word  count
# 0        국보    2.0
# 0     국보소년단    5.0
# 0       소년단    3.0
# 1       아줌마    3.0
# 2        팩트    2.0

#글자수가 2자이상인것만 추출합니다.

df_word = df_word.query('count >= 2')
print(df_word)

#        word  count
# 0        국보    2.0
# 0     국보소년단    5.0
# 0       소년단    3.0
# 1       아줌마    3.0
# 2        팩트    2.0

# 2글자 이상인것만 추출 되었습니다.
# 다음작업을 위해서 지금까지 정제된 데이터 df_word를 csv로 저장해 봅시다.
# time_pd2.to_csv("filename.csv", mode='a', header=False)
# df.to_csv("파일명", mode="", header=True|False)
df_word.to_csv("../Data/bts.csv", header=True, mode="w")
print("저장하였습니다.")

