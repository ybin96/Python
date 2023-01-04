import re
import requests


f = open('./Data/newbook.csv', "w", encoding="utf-8")
url = 'https://www.hanbit.co.kr/store/books/new_book_list.html'
text = requests.get(url).text
#<p class="book_tit"><a href="(.+?)">.+?</a></p>
list = re.findall(r'<p class="book_tit"><a href="(.+?)">(.+?)</a></p>',text)
for link in list:
    url2 = 'https://www.hanbit.co.kr/{}'.format(link[0])
    bookname = link[1]
    bookname= bookname.replace('&#40;', '(')
    bookname= bookname.replace('&#41;', ')')
    text2 = requests.get(url2).text
    regdate = re.findall(r'<strong>출간 : </strong><span>(.+?)</span>.+?<strong>페이지',text2, re.DOTALL)
    # <strong>판매가 : </strong>.+?<strong>(.+?)</strong>.+?원
    price = re.findall(r'<strong>판매가 : </strong>.+?<strong>(.+?)</strong>.+?원',text2, re.DOTALL)
    # print( bookname, regdate[0], price[0])
    # print('-'*50)
    row = "{},{},{}\n".format(bookname, regdate[0], price[0])
    f.write(row)
f.close()
print('새책 정보를 수집하였습니다.')

