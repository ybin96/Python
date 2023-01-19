import pandas as pd
import numpy as np
from wordcloud import WordCloud
import konlpy
import re

text = open("../Data/movie_script.txt", encoding="UTF-8").read()
# print(text)
#한글 이외의 문자을 제거합니다.
text= re.sub('[^가-힣]',' ',text)

# print(text)
print(text)

#문자열로 부터 명사만 추출 해 봅시다.
hannanum = konlpy.tag.Hannanum()
nouns = hannanum.nouns(text)
print(nouns)



# java.lang.ArrayIndexOutOfBoundsException: Index 10000 out of bounds for length 10000
# 	at kr.ac.kaist.swrc.jhannanum.plugin.MajorPlugin.PosTagger.HmmPosTagger.HMMTagger.new_mnode(HMMTagger.java:354)
# 	at kr.ac.kaist.swrc.jhannanum.plugin.MajorPlugin.PosTagger.HmmPosTagger.HMMTagger.tagPOS(HMMTagger.java:143)
# 	at kr.ac.kaist.swrc.jhannanum.hannanum.Workflow.analyzeInSingleThread(Workflow.java:857)
# 	at kr.ac.kaist.swrc.jhannanum.hannanum.Workflow.analyze(Workflow.java:521)
# 	at kr.lucypark.jhannanum.comm.HannanumInterface.simplePos09(Unknown Source)

# 위와 같은 오류가 발생합니다.
# 아마도 Hannanum의 nouns함수가
#       일을 처리할 때에 내부적으로 list를 만드는 것 같아요
#       그런데 수집한 영화대본의 단어가 너무 많아 10000개를 훨씬 넘어서 일을 못하는 것같아요
#           10000개 이하가 되도록 조절해서 프로그래밍 해 봅시다.










