import requests
import re

f= open('./Data/naver.txt', "w", encoding='utf-8')
for i in range(1,3):
    url = 'https://kin.naver.com/search/list.naver?query=30%EB%8C%80%20%EC%B0%BD%EC%97%85&page={}'.format(i)
    text= requests.get(url).text
    text = re.findall(r'<ul class="basic1">(.+?)<div class="s_paging">', text, re.DOTALL)
    list = re.findall(r'<a href="(.+?)" target="_blank" class="_nclicks:kin.txt _searchListTitleAnchor">.+?</a>', text[0])
    data = ""
    for link in list:
        text = requests.get(link).text
        q = re.findall(r'<div class="c-heading _questionContentsArea c-heading--default-old">(.+?)<div class="tag-list tag-list--end-title" role="region" aria-label="관련태그 목록" data-select="type-a">',text,re.DOTALL)
        a = re.findall(r'<div class="_answerListArea view-list view-list__card"(.+?)<a href="#" id="nextPageButton"', text, re.DOTALL)
        if len(q) > 0:
            data += q[0]
        if len(a) > 0:
            data += a[0]

    data = re.sub('<div_id="answer_1"', '' , data)
    data = re.sub('[0-9]','',data)
    data = re.sub('<.+?>','',data)
    data = re.sub(r'[~!@#$%^&*()+{}<>?/]+', '', data)
    data = re.sub(r'div id="answer " class="answer-content item contentWrap answer"[.]+div class="career item hiddenActivity" style="display: block"', '', data)
    data = re.sub(r'path fill="af" d="M l Ha -vc hl--c--- a l-a -l--a - "', '', data)
    data = re.sub(r'div class="card inner "[.]+채택답변수', '', data)
    data = re.sub(r'[A-Za-z]','',data)
    data = data.replace('.',"")
    data = data.replace("-","")
    data = data.replace("=","")
    data = data.replace("\"","")

    data = re.sub("\s", "_", data)
    data = re.sub('_+'," ",data)
    f.write(data+"\n")
    print("{}페이지를 다운받았습니다.".format(i))
