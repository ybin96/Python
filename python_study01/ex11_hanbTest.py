from hanb import bookInfo
import urllib.request
from bs4 import BeautifulSoup
import json

#한빛 출판사의 새로나온 책의 모든 정보(도서명,저자,출간일,페이지수,가격)를 출력 해 봅니다. 완성하면 "1"
# url = "https://www.hanbit.co.kr/store/books/look.php?p_code=B1068448075"

# info = bookInfo(url)
# print(info)

url = 'https://www.hanbit.co.kr/store/books/new_book_list.html'

flag = True
while flag:
    html = urllib.request.urlopen(url)
    bs_obj = BeautifulSoup(html, 'html.parser')
    # print(bs_obj)

    next = bs_obj.find_all('a',{'class':'next'})
    # print(next['href'])
    if len(next) != 0:
        url  = "https://www.hanbit.co.kr/"+next[0]['href']
        # print(url)
    else:
        flag = False

print('end')
paginate = bs_obj.find('div',{'class':'paginate'})
lastPage = ""
a_list = paginate.find_all("a")
if len(a_list)== 1:
    lastPage = paginate.find('strong').text
else:
    lastPage =a_list[-1].text
# print(lastPage)

lastPage = int(lastPage)

list = []
# for page in range(1,lastPage+1):
for page in range(1,4):
    url = "https://www.hanbit.co.kr/store/books/new_book_list.html?page={}&brand=&cate1=&cate2=&searchKey=&keyWord=".format(page)
    html = urllib.request.urlopen(url)
    bs_obj = BeautifulSoup(html, 'html.parser')
    #https://www.hanbit.co.kr/store/books/look.php?p_code=B6692242359
    detail_url_list = bs_obj.find_all('span',{'class':'pop_quick_bg'})
    for row in detail_url_list:
        detail_url = row['onclick']
        detail_url = detail_url.replace('location=','')
        detail_url = "https://www.hanbit.co.kr"+detail_url.replace('\'','')
        info = bookInfo(detail_url)
        list.append(info)
        # print(info)
    print("{}페이지를 수집하였습니다.".format(page))
result = {}
result['book_list'] = list
print(result)
print(len(list))

# string -> json            : loads
# json  ->                  : dumps
data = json.dumps(result)
f = open('./Data/newbook.json',"w",encoding='UTF-8')
f.write(data)
f.close()
print('파일을 생성하였습니다.')





