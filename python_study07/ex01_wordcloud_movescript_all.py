import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import konlpy
import re

f = open("../Data/movie_script.txt", encoding="UTF-8")

rows = f.readlines()
# print(len(rows))
# 3324
hannanum = konlpy.tag.Hannanum()
i = 1
data = ""
all = []



for row in rows:
    data = data + row
    i = i + 1
    if i % 100 == 0:
        # print(i,"-------------------------------------------------------")
        # print(data)
        data = re.sub('[^가-힣]', ' ', data)        
        nouns = hannanum.nouns(data)
        all = all + nouns
        # print(nouns)
        data = ""

print(all)

#불용어를 삭제 해 줍니다.
stopword = ["철기","주양","이동석"]
all = [i for i in all if i not in stopword]

# for w in stopword:
#     all.remove(w,)



#명사만 추출된 all 리스트를 데이터프레임으로 만들어요
df_word = pd.DataFrame({'word':all})
print(df_word)

#두글자 이상인 단어만 추출하기 위하여 글자길이 속성을 추가합니다.
df_word['count'] = df_word['word'].str.len()
print(df_word)

#글자길이 2글자 이상인 것만 추출합니다.
df_word = df_word.query('count >= 2')
print(df_word)

#단어별 빈도수를 구한 데이터프레임을 만들어요.
df_word = df_word.groupby('word', as_index=False)\
                .agg(n = ('word','count'))\
                .sort_values('n', ascending=False)

print(df_word.head(20))

#워드클라우드를 그리기 위해서 위의 데이터프레임을 딕셔너리로 만들어요
dic_word = df_word.set_index('word').to_dict()['n']
print(dic_word)

#워드클라우드를 그리기 위하여 워드클라우드 객체를 생성합니다

wc = WordCloud(
    random_state=1234,
    font_path="../Data/DoHyeon-Regular.ttf",
    width=400,
    height=400,
    background_color="white"
)

#워드클라우드에 표시할 단어별 빈도수가 있는 데이터를 설정합니다.
img_wordcloud = wc.generate_from_frequencies(dic_word)

#워드클라우드를 화면에 그립니다.
plt.Figure(figsize=(10,10))
plt.axis('off')
plt.imshow(img_wordcloud)
# plt.show()
plt.savefig("../Data/movie.png")
print("OK")











