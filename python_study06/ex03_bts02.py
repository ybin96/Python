import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import konlpy
from wordcloud import WordCloud

df_word = pd.read_csv("../Data/bts.csv", encoding="UTF-8")
print(df_word)
df_word =  df_word[['word','count']]
print(df_word)

#단어별 빈도수 파생변수를 만들고
#빈도수가 높은순으로 정렬합니다.
df_word = df_word.groupby('word', as_index=False)\
    .agg(n = ('word', 'count'))\
    .sort_values("n", ascending=False)

print(df_word)

#상위 몇개의(20개)의 데이터를 확인하고 불용어 처리 합니다.
top20 = df_word.head(20)
print(top20)

#상위 20개의 데이터를 막대그래프로 그려 봅니다.
#한글 설정
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

import seaborn as sns
sns.barplot(data=top20, x='n', y='word')
# plt.show()

#워드클라우드로 표현하기 위하여 데이터프레임을 딕셔너리로 만들어요
dic_word = df_word.set_index('word').to_dict()['n']
print(dic_word)
# {'축하': 236, '최고': 235, '자랑': 205, '면제': 173, '대한민국': 162, '대한': 162, '민국': 162, '군면제': 150, '보드': 131, '우리': 69, '선양': 63, '노래': 50, '국위': 45, '세계': 36, '양국': 35, '아미': 35, '소식': 31, '시기': 30, '생각': 30, '정국': 29, '행복': 29, '사람': 29, '사랑': 28, '역사': 28, '라니': 28, '코로나': 27, '생일': 27, '차트': 27, '핫백': 25, '국위선양국위선양': 24, '위라니': 24, '감사': 24, '전세계': 22, '미국': 22, '선양선양': 22, '진심': 22, '국위선양국위': 22, '이것': 22, '인정': 22, '싱글': 22, '그룹': 22, '정도': 22, '축하해': 21, '노력': 21, '응원': 20, '위선': 20, '활동': 19, '음악': 19, '고생': 18, '요즘': 18, '최초': 17, '아이': 17, '이제': 16, '국가': 16, '때문': 15, '올림픽': 15, '너희': 15, '양국위선양선양': 15, '문화': 15, '뉴스': 15, '기사': 14, '숟가락': 14, '기분': 14, '내가': 14, '수고': 14, '국민': 14, '멤버': 14, '대통령': 14, '마이트': 13, '아티스트': 13, '이름': 13, '시국': 13, '눈물': 13, '국뽕': 12, '금메달': 12, '댓글': 12, '시대': 12, '아시아': 12, '지금': 11, '하다': 11, '남자': 11, '다이': 11, '친구': 11, '싱글차트': 11, '기록': 11, '위로': 11, '재인': 11, '문재인': 10, '하나': 10, '만큼': 10, '병역': 10, '선물': 10, '사상': 10, '대표': 10, '국내': 10, '마라': 10, '진정': 9, '이번': 9, '재앙': 9, '인기': 9, '얘기': 9, '그것': 9, '희망': 9, '역사상': 9, '하루': 9, '케이': 9, '단하': 9, '세계적': 8, '군면제면제': 8, '오늘': 8, '가사': 8, '콩쿨': 8, '동안': 8, '케이팝': 8, '의미': 8, '시절': 8, '홍보': 8, '하자': 8, '정상': 8, '애국': 8, '데뷔': 8, '청와대': 8, '아이돌': 8, '경사': 8, '덕분': 8, '계속': 8, '누구': 7, '감격': 7, '소름': 7, '자리': 7, '경제': 7, '한번': 7, '효과': 7, '의무': 7, '여기': 7, '보이': 7, '얘들': 7, '정치': 7, '실력': 7, '월드컵': 7, '앨범': 7, '영향력': 7, '이상': 7, '일본': 7, '위상': 7, '기간': 6, '우울': 6, '월드': 6, '마음': 6, '아들': 6, '건강': 6, '동시대': 6, '모두': 6, '거지': 6, '세금': 6, '독도': 6, '사이': 6, '이젠': 6, '대한민국인': 6, '멜론': 6, '순위': 6, '외국': 6, '가치': 6, '외교': 6, '영광': 6, '영어': 6, '결국': 6, '블랙': 6, '처음': 6, '밴드': 6, '아침': 6, '쾌거': 6, '다음': 6, '아무': 6, '다이너마이트': 6, '시작': 5, '대한민국를': 5, '대중': 5, '성장': 5, '도움': 5, '기쁨': 5, '발표': 5, '레전': 5, '메인': 5, '메달': 5, '보유국': 5, '시민': 5, '그래미': 5, '이거': 5, '업적': 5, '기부': 5, '순간': 5, '기생충': 5, '기자': 5, '니들': 5, '문제': 5, '완전': 5, '와우': 5, '대상': 5, '영원': 5, '속보': 5, '무엇': 5, '역사적': 5, '나이': 5, '시간': 5, '여자': 5, '여러분': 5, '애국자': 5, '스타': 5, '국가대표': 5, '하면': 5, '개월': 5, '국를': 5, '가요': 5, '트롯': 5, '존경': 5, '결과': 5, '필요': 5, '축하축하': 5, '국격': 5, '청년': 5, '진입': 5, '해외': 5, '훈련': 5, '주세': 5, '거기': 5, '히트': 5, '경제적': 5, '추카': 5, '발매': 4, '유명': 4, '문통': 4, '세상': 4, '대체': 4, '챠트': 4, '가지': 4, '기대': 4, '정부': 4, '혜택': 4, '초청': 4, '한글': 4, '자기': 4, '방시': 4, '방시혁': 4, '주자': 4, '나중': 4, '나의': 4, '주라': 4, '병역면제': 4, '중요': 4, '영국': 4, '꽃길': 4, '사회': 4, '번째': 4, '손실': 4, '얘네들': 4, '영화': 4, '예술': 4, '존재': 4, '감동': 4, '기회': 4, '년만': 4, '투표': 4, '기초': 4, '새벽': 4, '해라': 4, '이래': 4, '국제': 4, '마지막': 4, '재능': 4, '추카추카': 4, '이용': 4, '군사': 4, '가도': 4, '이유': 4, '무대': 4, '축구': 4, '성과': 4, '모습': 4, '이후': 4, '실화': 4, '인생': 4, '팬덤': 4, '자체': 4, '가슴': 4, '국방': 4, '힐링': 4, '이네': 4, '그대': 4, '경제효과': 4, '문씨': 4, '비교': 4, '선수': 4, '비틀즈': 4, '문재앙': 4, '딴것': 3, '다이나': 3, '카디비': 3, '다이나마이트': 3, '시상식': 3, '겹경사': 3, '보드차트': 3, '넘사벽': 3, '준호': 3, '얼굴': 3, '시장': 3, '다행': 3, '언론': 3, '디피씨': 3, '코로나때문': 3, '신곡': 3, '얘네': 3, '어디': 3, '보드핫백': 3, '빅히트': 3, '애국시민': 3, '수십': 3, '스타일': 3, '느낌': 3, '최근': 3, '아시아인': 3, '블랙핑크': 3, '강경': 3, '데뷔때': 3, '승승장구': 3, '청춘': 3, '스포츠': 3, '아저씨': 3, '쓰럽': 3, '큰일': 3, '입대': 3, '본인': 3, '사벽': 3, '안해': 3, '복무': 3, '참고': 3, '찬성': 3, '최소': 3, '보이밴드': 3, '게임': 3, '보이그룹': 3, '강남스타일': 3, '하세': 3, '하루종일': 3, '보답': 3, '쟤들': 3, '미스': 3, '해주자': 3, '성적': 3, '대형': 3, '가요계': 3, '파이': 3, '유일': 3, '유튜브': 3, '가야': 3, '파이팅': 3, '국가적': 3, '의사': 3, '적폐': 3, '그동안': 3, '이도': 3, '대회': 3, '이랑': 3, '군인': 3, '핑크': 3, '막내': 3, '성공': 3, '인간적': 3, '국방부': 3, '휴가': 3, '국회': 3, '가능': 3, '국보': 3, '국익': 3, '국위선양': 3, '표현': 3, '정권': 3, '미국인': 3, '대중가요': 3, '오빠': 3, '보고': 3, '걱정': 3, '생활': 3, '공연': 3, '주면': 3, '역할': 3, '라디오': 3, '간만': 3, '병무청': 3, '영어권': 3, '종일': 3, '특별': 3, '옛날': 3, '오랜만': 3, '예전': 3, '현실': 3, '기초군사훈련': 3, '리스트': 3, '상상': 3, '정신': 3, '우승': 3, '관왕': 3, '튜브': 3, '요새': 3, '방법': 3, '외화': 3, '삼성': 3, '완벽': 3, '사고': 3, '한남': 2, '피땀': 2, '생일날': 2, '하지': 2, '한명': 2, '생일선물': 2, '상승': 2, '행보': 2, '사건': 2, '바리': 2, '바다': 2, '믹스': 2, '미스터': 2, '홍보대사': 2, '획득': 2, '뮤지션': 2, '뮤비': 2, '문화적': 2, '문죄인': 2, '후보': 2, '문대통령': 2, '무능': 2, '목적': 2, '모름': 2, '모든': 2, '훈련소': 2, '명곡': 2, '훈장': 2, '메세지': 2, '메달딴것': 2, '머리카락': 2, '바래요': 2, '박수': 2, '빈국': 2, '반감': 2, '빅뱅': 2, '비티에스': 2, '부탁': 2, '부존자원': 2, '부족': 2, '부담': 2, '봉준호': 2, '본고장': 2, '해용': 2, '보물': 2, '보드핫': 2, '보드싱글': 2, '해주고': 2, '병역특례': 2, '벤치': 2, '벌이': 2, '버스': 2, '행사': 2, '백만': 2, '방포': 2, '반대': 2, '생일축하': 2, '실시간': 2, '선구자': 2, '정치얘기': 2, '전정국': 2, '위버스': 2, '젊은이': 2, '정국이도': 2, '위기': 2, '정말': 2, '월드스타': 2, '워드': 2, '운동선수': 2, '운동': 2, '정수기': 2, '정의': 2, '정작': 2, '정치인': 2, '전역': 2, '말자': 2, '정치적': 2, '외화벌이': 2, '제대': 2, '제목': 2, '제일': 2, '조금': 2, '조선': 2, '오랫만': 2, '죄인': 2, '영웅': 2, '주가': 2, '영상': 2, '전원': 2, '위치': 2, '선배': 2, '이해': 2, '자랑쓰런': 2, '자부심': 2, '자신': 2, '일위': 2, '일본인': 2, '인지도': 2, '자원': 2, '인재': 2, '인성': 2, '인사': 2, '인물': 2, '인권': 2, '인간': 2, '작년': 2, '윈윈': 2, '잘못': 2, '이정': 2, '이의': 2, '이면': 2, '재능기부': 2, '전국민': 2, '의원': 2, '전달': 2, '전드': 2, '전부': 2, '음원': 2, '음악적': 2, '유럽': 2, '주고': 2, '열광': 2, '연예인': 2, '수상': 2, '축제': 2, '축하해용': 2, '신경': 2, '취향': 2, '칭찬': 2, '컴백': 2, '콘서트': 2, '시고': 2, '스트리밍': 2, '클래식': 2, '키즈': 2, '텃세': 2, '수식어': 2, '수가': 2, '연기': 2, '손흥민': 2, '테러': 2, '소통': 2, '소개': 2, '특례': 2, '세계인': 2, '세계문화': 2, '파구': 2, '파급': 2, '팩트': 2, '설명': 2, '평생': 2, '포방포': 2, '쓰럽게': 2, '아니쥬': 2, '아마': 2, '아빠': 2, '주모': 2, '역대': 2, '주변': 2, '주시': 2, '여건': 2, '주신': 2, '엑스': 2, '주의': 2, '에스': 2, '언플': 2, '억정': 2, '어이': 2, '증명': 2, '지네': 2, '지도': 2, '지붕': 2, '지원': 2, '암울': 2, '안티': 2, '안보': 2, '안됨': 2, '악플러들': 2, '철수': 2, '아이디': 2, '초대': 2, '최고최고': 2, '아시안': 2, '머리': 2, '가게': 2, '힘내': 2, '등극': 2, '개인': 2, '도로': 2, '난리': 2, '리스': 2, '관련주': 2, '단군이래': 2, '리스펙': 2, '단비': 2, '나스': 2, '나무': 2, '강제': 2, '리얼': 2, '관광객': 2, '덤핑': 2, '그래미상': 2, '끝물': 2, '고민': 2, '꼰대': 2, '마니': 2, '당신': 2, '감사해': 2, '김석진': 2, '마세': 2, '마이클': 2, '마이클잭': 2, '그네': 2, '기획사': 2, '그때': 2, '단군': 2, '개인적': 2, '국제콩쿨': 2, '광고': 2, '국개의원': 2, '드로': 2, '격과': 2, '국가홍보': 2, '디피': 2, '년전': 2, '국보급': 2, '능가': 2, '겸손': 2, '네이버': 2, '넘버원': 2, '거리': 2, '래요': 2, '경비대': 2, '다운': 2, '갱신': 2, '동급': 2, '레전드': 2, '돌이': 2, '레전드로': 2, '경제적가치': 2, '개판': 2, '교육': 2, '국적': 2, '경제적효과': 2, '로드': 2, '독보적': 2, '과거': 2, '강남': 2, '국격과': 2, '기여': 2, '기업': 2, '말구': 2, '근무': 2, '공익': 2, '고장': 2, '고통': 2, '기간동안': 2, '대사': 2, '공부': 2, '기본적': 2, '가보': 2, '공감': 2, '곳곳': 2, '대중성': 2, '대신': 2, '글로벌': 2, '기억': 2, '기적': 2, '기자분': 2, '정구기': 1, '쟝르': 1, '정국군': 1, '쟤네': 1, '쟤네들': 1, '중앙일보': 1, '구리': 1, '중복투표': 1, '줄아시': 1, '중국': 1, '저기': 1, '정구': 1, '점심': 1, '점수': 1, '중앙': 1, '정국오빠': 1, '구도': 1, '중년': 1, '정국이의': 1, '재판대기중': 1, '줄세우': 1, '구기': 1, '교육후': 1, '정도로': 1, '줄기': 1, '정도일': 1, '공긍횡령': 1, '주훈련': 1, '재판': 1, '정밀': 1, '정복': 1, '교가': 1, '구봉': 1, '저번': 1, '국가차원': 1, '적대': 1, '중반': 1, '중복': 1, '적극': 1, '전세계최대시장': 1, '구한테': 1, '전성기': 1, '적인': 1, '전용기': 1, '전설': 1, '전생': 1, '국가대표급': 1, '전멤버': 1, '국가위상': 1, '국가적인': 1, '구한': 1, '구장': 1, '저질': 1, '저희': 1, '젊은얘들': 1, '중소기업': 1, '절반': 1, '절대': 1, '중단': 1, '전함': 1, '주죠': 1, '전원군면제': 1, '전파': 1, '전체': 1, '구속': 1, '전쟁': 1, '중독성': 1, '전자': 1, '주지': 1, '공직자': 1, '정부관계자': 1, '조원': 1, '조현': 1, '조차': 1, '조짐중': 1, '조짐': 1, '조직적': 1, '조종': 1, '조작': 1, '조심': 1, '조현병': 1, '과일': 1, '조단위더': 1, '조단': 1, '조나스': 1, '과한': 1, '조건': 1, '제일영웅': 1, '주둥이': 1, '조회': 1, '주류': 1, '과반수': 1, '좌파': 1, '공정': 1, '좌절': 1, '주구장창': 1, '좌익': 1, '좋가': 1, '주길': 1, '종례시간': 1, '조회수': 1, '종례': 1, '졸개': 1, '존재자체': 1, '과언': 1, '과의': 1, '주도': 1, '조회수로': 1, '공인': 1, '주만': 1, '광팬': 1, '공로': 1, '주요뉴스': 1, '공백': 1, '주일': 1, '정체': 1, '정찰': 1, '관심': 1, '주임': 1, '정의당': 1, '주심': 1, '관심을': 1, '정은경': 1, '정은': 1, '주간': 1, '광고효과': 1, '주정': 1, '정상적': 1, '주요': 1, '관리법': 1, '관계자': 1, '제가': 1, '제외': 1, '제어때': 1, '제어': 1, '관광': 1, '제대자': 1, '주말': 1, '제국': 1, '공수': 1, '공백기': 1, '정호석': 1, '정치충': 1, '공사기업': 1, '관광업': 1, '공사': 1, '관련': 1, '정치외교': 1, '주작': 1, '자제': 1, '국경': 1, '이놈': 1, '이름때문': 1, '군필자': 1, '이루': 1, '굴욕': 1, '굴욕외교': 1, '이때': 1, '이득': 1, '굿굿': 1, '이대': 1, '그거': 1, '재수': 1, '이기세가': 1, '이기': 1, '이거엄청': 1, '이가': 1, '그래미가면': 1, '의식': 1, '의민지': 1, '그레': 1, '의무적': 1, '이만치': 1, '이만큼': 1, '군필': 1, '이명': 1, '군면제찬성': 1, '군면제해라': 1, '군복': 1, '이전': 1, '이자': 1, '군복무': 1, '군복무대신': 1, '이용촬영': 1, '군사법원': 1, '이요': 1, '이성': 1, '군입대': 1, '이빨': 1, '군제대자': 1, '이바지': 1, '이미지': 1, '이문덕': 1, '이문': 1, '이명박이': 1, '그레미': 1, '그룹뿐': 1, '음활동': 1, '그해': 1, '유사': 1, '유발': 1, '유명하다': 1, '극찬': 1, '극한': 1, '유도': 1, '유닛': 1, '유니폼': 1, '유능': 1, '근래': 1, '위해': 1, '위지': 1, '위주죠': 1, '위정': 1, '위안': 1, '위생법': 1, '위상를': 1, '위상과': 1, '금년': 1, '유사이래': 1, '유일하다': 1, '그룹임': 1, '유일한': 1, '음악활동': 1, '음악캠프': 1, '그룹차트': 1, '음악역사': 1, '음악성': 1, '음악계': 1, '음악가': 1, '그릇': 1, '음방': 1, '음모': 1, '으헝헝헝': 1, '으헝': 1, '융성': 1, '윤미향': 1, '윤기': 1, '육군': 1, '유행': 1, '그중': 1, '유툽': 1, '이쯤': 1, '군면제인거잖': 1, '이행': 1, '자유': 1, '자연': 1, '자식': 1, '자세': 1, '국봉': 1, '자만': 1, '국뽕차': 1, '자로': 1, '자랑쓰럽': 1, '국수': 1, '자랑스럽군': 1, '자랑럽': 1, '국악': 1, '자대': 1, '국악대회': 1, '자격': 1, '있음': 1, '있는거잖아': 1, '입증': 1, '입상한': 1, '국방의무': 1, '중요성': 1, '입상': 1, '자존': 1, '재벌기업': 1, '재벌': 1, '국내대회': 1, '국대': 1, '장르': 1, '장년': 1, '장난': 1, '장관아들': 1, '장관': 1, '잘뽑앗더라': 1, '국문학': 1, '잘만': 1, '작품': 1, '작성': 1, '국민청원': 1, '작곡과': 1, '작곡가': 1, '국민투표': 1, '자존감': 1, '입상자': 1, '국운': 1, '군면제얘기': 1, '인트': 1, '인터넷': 1, '국제적': 1, '인증': 1, '인정이다': 1, '국회의원': 1, '인인': 1, '인아': 1, '군면제가도': 1, '군면제감': 1, '군면제급': 1, '군면제대상': 1, '인마': 1, '인데': 1, '인기확보': 1, '군면제리스트': 1, '군면제면제요청': 1, '인건': 1, '군면제사유': 1, '군면제생활': 1, '인터넷공급': 1, '인트로': 1, '임팩트': 1, '일가': 1, '임지': 1, '일주일간': 1, '일조': 1, '일장기부대': 1, '일장기': 1, '국위선양선양': 1, '일요일': 1, '일어': 1, '일상': 1, '일부': 1, '일본차': 1, '국위선양선향': 1, '일본도': 1, '일보': 1, '일베충': 1, '일루미': 1, '일루': 1, '일등': 1, '일곱': 1, '공급': 1, '지름길': 1, '중장년': 1, '피골': 1, '하늘': 1, '개신교': 1, '하긋': 1, '하거': 1, '하개': 1, '필자': 1, '필요하다': 1, '개인발표': 1, '피스': 1, '플러스': 1, '하단': 1, '프리메이슨': 1, '프리': 1, '개인주의야': 1, '퐉퐉': 1, '폭풍눈물': 1, '폭풍': 1, '폭파': 1, '폭락': 1, '포인트': 1, '개소리': 1, '개버전': 1, '거해': 1, '한마디': 1, '한탄': 1, '한창': 1, '한주': 1, '한정': 1, '한잔': 1, '한수': 1, '갓신인': 1, '한민족': 1, '강구': 1, '한류': 1, '개미': 1, '한둘': 1, '한데': 1, '한글가사': 1, '강남스타윌': 1, '한계': 1, '강제징병': 1, '개념': 1, '하면서': 1, '개념보고': 1, '포상금': 1, '개챠트': 1, '포기': 1, '트집': 1, '팅하세': 1, '티나': 1, '특수기간': 1, '특수': 1, '특별하다': 1, '특별귄한': 1, '거임': 1, '특례법': 1, '거잖': 1, '트를': 1, '폐렴시국': 1, '거쟈': 1, '트럼프': 1, '거지떼': 1, '거품': 1, '통일': 1, '통용': 1, '통닭': 1, '통과': 1, '토종': 1, '거말구': 1, '파구리': 1, '파도': 1, '파생': 1, '폐렴': 1, '평판': 1, '평등': 1, '평가': 1, '편승': 1, '편곡': 1, '펭수': 1, '페이지': 1, '팬임': 1, '팬분': 1, '개판소식': 1, '팩트체크': 1, '패거리': 1, '팝중': 1, '판소리': 1, '판사': 1, '판국': 1, '거랑': 1, '거론': 1, '한판': 1, '감흥': 1, '핫벡': 1, '환치기': 1, '황금막내': 1, '황금': 1, '활용': 1, '활성화': 1, '활력': 1, '활동임': 1, '활동시기': 1, '가장': 1, '활개': 1, '환멸': 1, '혼란': 1, '확보': 1, '화이팅되': 1, '화이팅': 1, '화력': 1, '화가': 1, '홍보사진': 1, '홍보도': 1, '가전': 1, '가족': 1, '회사': 1, '회수': 1, '가자': 1, '횡령': 1, '가관': 1, '히트침': 1, '히트곡': 1, '가기': 1, '희안': 1, '가락': 1, '희대': 1, '흥행': 1, '흑인인권운동': 1, '흑인': 1, '흑백명부': 1, '흑백': 1, '가면': 1, '가봐야겠어': 1, '가슴팍': 1, '후회': 1, '후원': 1, '가시길': 1, '가실': 1, '홈페이지': 1, '호중': 1, '핫샷': 1, '감사하다': 1, '핸드폰': 1, '핵처': 1, '핵인정': 1, '해지': 1, '갈말읍': 1, '해주심': 1, '해주세': 1, '해주라': 1, '감독': 1, '해외활동': 1, '호의적': 1, '해외팬': 1, '해외원정': 1, '해야': 1, '감회': 1, '해냈습니다': 1, '해냈고': 1, '해내': 1, '핫차트': 1, '핫샷데뷔': 1, '햇살': 1, '했어도': 1, '했잖': 1, '했잖야': 1, '호석': 1, '호르몬전쟁': 1, '호르몬': 1, '호들갑': 1, '가짜': 1, '형평': 1, '형님': 1, '현존': 1, '현재': 1, '현역': 1, '가짜뉴스': 1, '현대적': 1, '현대': 1, '헝헝': 1, '각종': 1, '행복하다': 1, '간에': 1, '행보기대': 1, '갈말': 1, '테리': 1, '건하': 1, '중학교': 1, '고유': 1, '처음봄': 1, '고요': 1, '처벌': 1, '고위': 1, '챠드': 1, '책내서': 1, '고위공직자': 1, '찬스': 1, '찬송': 1, '착륙': 1, '천대': 1, '차트아웃': 1, '고유명사': 1, '차지': 1, '차원': 1, '차로': 1, '쭵쭵': 1, '쫏빠리': 1, '쫏빠': 1, '쫏바리': 1, '천년만년': 1, '천만다행': 1, '털이': 1, '청원넣줘': 1, '초심': 1, '초록뱀': 1, '초록': 1, '초딩생': 1, '고뇌': 1, '체크': 1, '체납': 1, '청취자': 1, '고라니': 1, '청원': 1, '천배': 1, '고려': 1, '청와': 1, '청소년': 1, '철저': 1, '철원군': 1, '철원': 1, '철수형님': 1, '고생길': 1, '천번백번': 1, '쪽빠리': 1, '쪽바리': 1, '짱짱': 1, '지도자': 1, '지역행사': 1, '지역': 1, '곡중': 1, '지민': 1, '지리': 1, '위반카메라': 1, '지령': 1, '지디': 1, '지도층': 1, '지대': 1, '짱임': 1, '지금의': 1, '공개': 1, '지구': 1, '지경': 1, '지가': 1, '공공': 1, '증거': 1, '즈그땅': 1, '즈그들': 1, '곡식': 1, '지지율': 1, '지칭': 1, '지향점': 1, '징병제': 1, '징병': 1, '징계': 1, '집하': 1, '집콕': 1, '집안': 1, '집단': 1, '질투': 1, '진행': 1, '진출': 1, '진지': 1, '진영': 1, '진싱자랑': 1, '고통속': 1, '진실성': 1, '진골': 1, '직하': 1, '직접적': 1, '직장인': 1, '초월': 1, '초임': 1, '고고': 1, '결론': 1, '코스프레': 1, '코메디': 1, '코리아': 1, '코로나위기': 1, '코로나시국': 1, '겨를': 1, '케이팝거리': 1, '격하': 1, '케이크': 1, '컴플렉스': 1, '카메라': 1, '결실': 1, '컨트롤': 1, '컨셉': 1, '커리어': 1, '캡짱': 1, '캠프': 1, '캐나다': 1, '카테고리': 1, '카운트다운': 1, '겠숩': 1, '콩알탄': 1, '콩쿠': 1, '게이': 1, '터프': 1, '태어나줘': 1, '태도': 1, '태극기': 1, '태권도': 1, '탑스타': 1, '탈세': 1, '타자': 1, '타격': 1, '걷쟈': 1, '키보드': 1, '걸그룹': 1, '클래스': 1, '겉으론': 1, '큰상': 1, '크라스': 1, '퀄리티': 1, '게스트': 1, '콩쿨등': 1, '카운트': 1, '카르텔': 1, '초토화': 1, '계기': 1, '추카해': 1, '경제뉴스': 1, '추천': 1, '추억속': 1, '추억': 1, '쵝오': 1, '최초이자': 1, '최정상': 1, '최애': 1, '최대': 1, '카레': 1, '최단': 1, '최근노래': 1, '계단': 1, '계정': 1, '최고자랑': 1, '최고잋': 1, '최고이': 1, '계획': 1, '촬영': 1, '경인선가즈': 1, '축구경기': 1, '축배': 1, '경인': 1, '카디비의': 1, '결정': 1, '결탁': 1, '결혼': 1, '치진': 1, '치적': 1, '측면': 1, '취득': 1, '취급': 1, '충성충성': 1, '충성': 1, '출근길': 1, '춘천': 1, '경기': 1, '축하해요': 1, '경사낫': 1, '축하새': 1, '축하메시지': 1, '경의': 1, '금메달급': 1, '말길': 1, '위반': 1, '브리트': 1, '비난글': 1, '비난': 1, '동시': 1, '블럭': 1, '동양인': 1, '블랙코메디': 1, '블랙아이': 1, '블랙리스트': 1, '됬다': 1, '브로마이드': 1, '분홍': 1, '브랜드': 1, '브라더스': 1, '불쌍': 1, '불매운동': 1, '불매': 1, '불만': 1, '불과': 1, '불공정': 1, '불가능': 1, '비들': 1, '비례': 1, '비례대표': 1, '비리': 1, '빨갱이': 1, '빠져': 1, '빠리': 1, '빈집털이': 1, '빈집': 1, '독일': 1, '독일팬': 1, '비하': 1, '비티엑스': 1, '동기': 1, '비튀': 1, '비타민': 1, '비즈니스': 1, '비의': 1, '비웃음': 1, '비엔나': 1, '비상업적활동': 1, '비상': 1, '비버': 1, '불가': 1, '분탕': 1, '뻘짓': 1, '보삼': 1, '보이밴드중': 1, '등장이요': 1, '등판': 1, '등하': 1, '등하면': 1, '보유': 1, '보여': 1, '보약': 1, '보셈': 1, '보배': 1, '분야': 1, '보믄': 1, '디스코': 1, '딩시절': 1, '딴말': 1, '딸내미': 1, '보드도': 1, '때라': 1, '보도': 1, '때메': 1, '보이스': 1, '보태': 1, '보탬': 1, '보호': 1, '분과': 1, '북미': 1, '드높힘': 1, '부채': 1, '드뎌': 1, '부정': 1, '부여': 1, '부모': 1, '부르노마스': 1, '부대': 1, '듣기': 1, '봉준호감독': 1, '봉사역할': 1, '봉사': 1, '볼일': 1, '본적': 1, '등극한': 1, '등에': 1, '등장': 1, '빼액': 1, '뻘짖': 1, '대취타': 1, '대한민국위선양상': 1, '선가': 1, '서울': 1, '서양인': 1, '서양': 1, '생활속': 1, '생활면': 1, '대한민국어로': 1, '대한민국예술문화': 1, '생일추카': 1, '생일도': 1, '새꾸': 1, '대한민국인인': 1, '대한민국임': 1, '생시': 1, '생선': 1, '생계': 1, '생각지도': 1, '대한민국팬': 1, '새벽내': 1, '대형기획사때매': 1, '대한민국야': 1, '선두': 1, '대한민국아이돌': 1, '대한민국순위': 1, '성인': 1, '성실': 1, '성매매알선': 1, '성매매': 1, '대한민국가': 1, '성공한거처럼': 1, '대한민국그룹': 1, '설움': 1, '대한민국놈': 1, '선향': 1, '선택': 1, '선처': 1, '선정적': 1, '선정': 1, '선양해': 1, '대한민국를위': 1, '대한민국문화': 1, '대한민국사람': 1, '선봉': 1, '새끼': 1, '상한가': 1, '뻘짖거리': 1, '사모님': 1, '사절은': 1, '사재기': 1, '사이다': 1, '도댜체': 1, '사유': 1, '사용': 1, '사실': 1, '사생활': 1, '도입': 1, '사막': 1, '상한': 1, '도촬당': 1, '독도경비대': 1, '사단장급': 1, '사단장': 1, '사단': 1, '독도홍보': 1, '사건임': 1, '사가': 1, '뽕짝': 1, '사주': 1, '사주기초훈련': 1, '사진': 1, '사탄': 1, '상징': 1, '상접': 1, '상업적': 1, '대형브로마이드': 1, '상습': 1, '상상이상': 1, '댓가': 1, '상를': 1, '상도': 1, '상남자': 1, '상금': 1, '상관': 1, '상과': 1, '삼성전자': 1, '삼성오너일가': 1, '더블': 1, '살맛': 1, '사회지도층': 1, '사회주의': 1, '보내다': 1, '떡잎': 1, '병장': 1, '무료': 1, '마이트를': 1, '마이트인트': 1, '문꼰대': 1, '무지': 1, '무작정': 1, '무용': 1, '마인드': 1, '무시': 1, '무스': 1, '마찬가지': 1, '막내딸': 1, '무당': 1, '무늬': 1, '마카레나로': 1, '목표': 1, '마해라': 1, '모형': 1, '모집하겠숩': 1, '막강': 1, '모병': 1, '문장': 1, '문재': 1, '문재인대통령': 1, '문재인아': 1, '물타기': 1, '물뽕': 1, '물론': 1, '물건': 1, '문화훈장': 1, '문화쪽': 1, '문화전파': 1, '마사': 1, '문화외교관': 1, '문화외교가': 1, '마사오': 1, '문학': 1, '문프': 1, '문통과': 1, '마스': 1, '문죄앙': 1, '문죄': 1, '문제인': 1, '마이': 1, '모범': 1, '모든이': 1, '병역혜택': 1, '멋지네': 1, '메이커': 1, '메이저': 1, '메이슨': 1, '메시지': 1, '만세': 1, '메달획득': 1, '만이': 1, '만찬': 1, '멍충이': 1, '먹자': 1, '모든분': 1, '만회': 1, '매인탑뉴스': 1, '매인': 1, '매매': 1, '매니아': 1, '맞져': 1, '망정': 1, '말기': 1, '말로': 1, '만명': 1, '메인뉴스': 1, '메인싱글': 1, '메인음원차트': 1, '막둥이': 1, '막둥이정국': 1, '모너모': 1, '모너': 1, '몇십': 1, '몇백만': 1, '명예': 1, '명사': 1, '명부': 1, '만기': 1, '면죄': 1, '면제가지마라': 1, '만기전역': 1, '멤버간': 1, '만달러': 1, '멜론차트': 1, '만도': 1, '멜로디': 1, '메인차트': 1, '뭉디': 1, '마무리': 1, '마룬': 1, '련아': 1, '백성': 1, '백배': 1, '백만배': 1, '배철수': 1, '배우자': 1, '배우기': 1, '배경': 1, '방영': 1, '레코드': 1, '방송국': 1, '뮤직': 1, '방송': 1, '방뽕': 1, '로도': 1, '방기': 1, '밥상': 1, '로스': 1, '발라드': 1, '반영': 1, '반백살': 1, '백스트리트': 1, '백인': 1, '레벨': 1, '밴드중': 1, '라가': 1, '라도': 1, '병역기간동안': 1, '라면': 1, '라스': 1, '변절자': 1, '변신': 1, '랑해': 1, '벙역': 1, '법원': 1, '법안': 1, '범주': 1, '범죄': 1, '범접불가': 1, '범접': 1, '런던': 1, '번갈': 1, '버전': 1, '런식': 1, '반백': 1, '반만큼': 1, '롱런': 1, '민방위': 1, '민간외교': 1, '민간': 1, '믹스테잎': 1, '리오도': 1, '미필': 1, '미통닭': 1, '미쿡서': 1, '미쿡': 1, '미쳣': 1, '미제': 1, '미스트롯': 1, '미스테리': 1, '미스터트롯': 1, '린지': 1, '미분': 1, '미래': 1, '마돈나': 1, '미국령': 1, '마련': 1, '민도': 1, '민스트라': 1, '반값': 1, '민윤기': 1, '르노': 1, '박진영': 1, '박지민': 1, '박지': 1, '박장대소': 1, '박장': 1, '박이': 1, '박약': 1, '를위': 1, '박그네': 1, '리믹스': 1, '바람': 1, '바디친구밖': 1, '바디': 1, '바닥': 1, '밑바닥': 1, '민지': 1, '민주인사': 1, '민주': 1, '대통령령': 1, '성폭력': 1, '위못': 1, '엊그제': 1, '남녀': 1, '여건등': 1, '남미': 1, '엠카운트다운': 1, '엔싱크': 1, '낭비': 1, '에어로스미스': 1, '에어로': 1, '내고': 1, '내면': 1, '내주': 1, '업로드': 1, '업데이트': 1, '업그레이드': 1, '엄마': 1, '내서': 1, '얹을려': 1, '내야': 1, '언제': 1, '언어': 1, '여기저기': 1, '여대': 1, '날리': 1, '여서도': 1, '나도': 1, '연주': 1, '연예인중': 1, '나로': 1, '연예란': 1, '연말': 1, '역쉬': 1, '역사책': 1, '나스엑스': 1, '역사이다': 1, '역사이기도': 1, '나이스': 1, '역사가': 1, '역대급인건': 1, '역대급': 1, '난리치진': 1, '난리통': 1, '여성인권': 1, '여성': 1, '언론쓰레기': 1, '내주세요': 1, '열망': 1, '노해': 1, '애국아이돌': 1, '년차': 1, '노노해': 1, '노무': 1, '알탄': 1, '알선': 1, '안했어도': 1, '안해주지': 1, '안해주면': 1, '논밭': 1, '억이상': 1, '안지': 1, '안전': 1, '논의': 1, '놀람': 1, '안가': 1, '놀림': 1, '악플러': 1, '악플': 1, '악질좌파': 1, '애미': 1, '년도': 1, '앨범차트': 1, '년대': 1, '억겹': 1, '어줍짢': 1, '어제': 1, '넘넘': 1, '어머': 1, '어른': 1, '어로': 1, '어려움': 1, '어깨': 1, '넘버원송': 1, '녀석': 1, '얘내들': 1, '얘기해': 1, '년간': 1, '양해': 1, '양상': 1, '양복': 1, '양를': 1, '년기간': 1, '열등감': 1, '열매': 1, '성폭력범죄': 1, '우스갯소리': 1, '울대': 1, '운해': 1, '운운': 1, '운로드': 1, '기덕': 1, '기도': 1, '우월감': 1, '기레': 1, '우시국': 1, '우리집': 1, '외국인': 1, '기부체납': 1, '우끼끼': 1, '요청': 1, '요즘대세인': 1, '요즘대세': 1, '기사도': 1, '요소': 1, '외환관리법': 1, '외환': 1, '웃음거리': 1, '워너비': 1, '기대이상': 1, '말대': 1, '금메달리스트': 1, '금융': 1, '위도': 1, '위더': 1, '위대': 1, '위기사라니': 1, '금의': 1, '위곡': 1, '위가도': 1, '웬일': 1, '월드스타를': 1, '기념': 1, '월드그룹밴드': 1, '기념비': 1, '월급': 1, '원정': 1, '원숭이': 1, '원망': 1, '원디렉션': 1, '외화획득': 1, '외국아미': 1, '열정적': 1, '영향': 1, '예점': 1, '김연아선수': 1, '예언': 1, '예술쪽': 1, '예술분야': 1, '예술가': 1, '김태형': 1, '김호중': 1, '꼬라지': 1, '꼬레': 1, '외교적': 1, '꼬리표': 1, '영어라': 1, '영어노래': 1, '꼭두각시': 1, '영어가사': 1, '꼭지': 1, '꿈애': 1, '염색': 1, '염불하던것들': 1, '오너': 1, '김대중대통령': 1, '오늘만큼': 1, '오도': 1, '외교관': 1, '외교가': 1, '왕관': 1, '완전체': 1, '기존': 1, '완장': 1, '기준': 1, '와의': 1, '올해': 1, '길이': 1, '올드': 1, '온몸': 1, '온라인': 1, '오졋': 1, '오스카': 1, '김기덕': 1, '김남': 1, '김대중': 1, '오라': 1, '악질': 1, '악수': 1, '아픔': 1, '수천': 1, '숭배': 1, '술장사': 1, '대대손손': 1, '대댜': 1, '순시리': 1, '순시': 1, '대빅': 1, '수천억': 1, '수천만': 1, '수익금': 1, '수기': 1, '수익': 1, '수원': 1, '수십배': 1, '수십년동안': 1, '수십년': 1, '대서특필': 1, '대성': 1, '수비대': 1, '수록': 1, '숭배영상': 1, '숮가락': 1, '쉬레': 1, '스리': 1, '스피어스': 1, '스프': 1, '스펙': 1, '스페인': 1, '스틴비버': 1, '스틴': 1, '스트리퍼': 1, '스트리트': 1, '대기': 1, '스트라': 1, '스탭분': 1, '스탭': 1, '대대': 1, '가격': 1, '스을적': 1, '스을': 1, '스웨텐팝': 1, '스밍': 1, '스미스': 1, '수로': 1, '대성하세욜': 1, '아티스트라': 1, '대조적': 1, '세일': 1, '세인': 1, '세우': 1, '세요': 1, '대장주': 1, '세금탈세': 1, '대접': 1, '세계최고': 1, '세계정복': 1, '대중문화': 1, '대세': 1, '세계음악시장': 1, '세계아미': 1, '세계시장': 1, '세계속': 1, '세계문화대통령': 1, '세계대회': 1, '대중적': 1, '세가': 1, '성향': 1, '세팅': 1, '센스': 1, '대장': 1, '소녀단': 1, '송익필': 1, '송강': 1, '손흥민도': 1, '대소': 1, '손해지': 1, '손해': 1, '손발': 1, '대영': 1, '소향': 1, '대영제국': 1, '소신': 1, '소식임': 1, '대운': 1, '소속사가': 1, '소속': 1, '소린지': 1, '소리': 1, '대응': 1, '소년': 1, '승리': 1, '당대': 1, '담주': 1, '능력': 1, '뉴키즈온더블': 1, '아시': 1, '느켰습니': 1, '아부아첨': 1, '아부': 1, '아바': 1, '아미팬': 1, '아미분': 1, '아미님': 1, '다가': 1, '닭그네정부': 1, '아래': 1, '아랑곳': 1, '다나': 1, '다양': 1, '쓰레기': 1, '다양성': 1, '다에': 1, '쌩신인': 1, '쌉인정': 1, '아시아위주임': 1, '뉴키즈': 1, '뉴스란': 1, '아시안게임': 1, '놀이터': 1, '아킬레스건': 1, '아카데미': 1, '누구도': 1, '아첨': 1, '아줌마': 1, '아저씨단': 1, '누군가': 1, '아이콘': 1, '아이러니하다': 1, '아이러니': 1, '눈높이': 1, '아이돌팬': 1, '아이돌이균': 1, '아이돌이': 1, '눈면제': 1, '뉴스라니': 1, '아웃': 1, '아시안게임금메달': 1, '쌉인': 1, '싸인': 1, '싱크': 1, '단계': 1, '식품위생법': 1, '식품': 1, '시초': 1, '단발성': 1, '시스템': 1, '단체': 1, '시사뉴스': 1, '시사': 1, '시바노무': 1, '시바': 1, '시민단체': 1, '단하디': 1, '시도로': 1, '시대때': 1, '단합': 1, '시기질투': 1, '달러': 1, '달성': 1, '시고하진': 1, '신고': 1, '신기': 1, '싱글앨범': 1, '신기루': 1, '다음기회': 1, '십원': 1, '심하단': 1, '심장': 1, '다음성적': 1, '실질적': 1, '실제적': 1, '실제': 1, '다음주': 1, '실상': 1, '실망': 1, '실리적': 1, '실력있음': 1, '다음주면': 1, '신화': 1, '신중': 1, '신인': 1, '신드롬': 1, '신기방기': 1, '워인': 1}

#워드클라우드 모양을 위한 mask로 사용할 객체를 생성합니다.
import PIL
icon = PIL.Image.open("../Data/heart.png")

img = PIL.Image.new("RGB", icon.size, (255,255,255))
img.paste(icon,icon)
img = np.array(img)

font = "../Data/DoHyeon-Regular.ttf"

wc = WordCloud(
    random_state=1234,
    font_path=font,
    width=400,
    height=400,
    background_color='white',
    mask=img
)

img_wordcloud = wc.generate_from_frequencies(dic_word)

plt.figure(figsize=(10,10))
plt.axis('off')
plt.imshow(img_wordcloud)
plt.show()














