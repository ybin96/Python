import re
import urllib.request
from bs4 import BeautifulSoup
import requests
import json

url = "https://smartstore.naver.com/i/v1/reviews/details?reviewIds[]=4159616459,4162153844,4117852305,4152355291&merchantNo=510159484"
text = requests.get(url).text
print(text)
print(type(text))
data = json.loads(text)
# print(type(data))
# a = data[0]
# print(a)
# print(type(a))
# reviewContent = a['reviewContent']
# print(reviewContent)
# reAttatch = a['repThumbnailTagNameDescription']['attachDescription']
# print("-"*50)
# print(reAttatch)

f = open('./Data/sundae.txt', "w", encoding="utf-8")
for a in data:
    reviewContent = a['reviewContent']
    rep = a['repThumbnailTagNameDescription']
    f.write(reviewContent+"\n")
    if rep:
        attach = rep['attachDescription']
        f.write(attach+"\n")

f.close()
print('순대에 대한 리뷰를 수집하였습니다.')














