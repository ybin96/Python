import re
import requests

url = 'https://www.hanbit.co.kr/store/books/new_book_list.html'
text = requests.get(url).text
# print(text)

'''
<!-- 페이징 -->
    <div class="paginate">
      <a href="/store/books/new_book_list.html?page=80&brand=&cate1=&cate2=&searchKey=&keyWord=" class="pre"><span>&lt;</span> </a>
<strong>81</strong>
    </div>
    <!-- //페이징 -->
'''

flag = True

while flag:
    next = re.findall(r'<a href="(.+?)" class="next"><span>&gt;</span></a>', text)
    print(next)
    if len(next) == 0:
        pages= re.findall(r'<div class="paginate">.+?<a href=".+?">(.+?)</a>.+?<!-- //페이징 -->', text, re.DOTALL)
        if len(pages) == 1:
            lastPage = re.findall(r'<!-- 페이징 -->.+?<strong>(.+?)</strong>.+?<!-- //페이징 -->', text, re.DOTALL)
        else:
            lastPage = pages[len(pages)-1]
        flag=False
    else:
        url = 'https://www.hanbit.co.kr{}'.format(next[0])
        text=requests.get(url).text
lastPage = int(lastPage[0])
print("마지막페이지:",lastPage)

# <div class="paginate">.+?<a href="(.+?)" class="next">
# next = re.findall(r'<a href="(.+?)" class="next"><span>&gt;</span></a>.+?</div>', text, re.DOTALL)
# for row in next:
#     print(row)




f = open('./Data/newbook.csv', "w", encoding="utf-8")

for page in range(1,lastPage-1):
    url = 'https://www.hanbit.co.kr/store/books/new_book_list.html?page={}&brand=&cate1=&cate2=&searchKey=&keyWord='.format(page)
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
    print('{}페이지의 내용을 수집하였습니다.'.format(page))

f.close()
print('새책 정보를 모두 수집하였습니다.')

