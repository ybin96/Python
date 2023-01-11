import urllib.request
import bs4

url = "https://www.hanbit.co.kr/store/books/new_book_list.html"
html= urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, 'html.parser')
# print(bs_obj)
title_list = bs_obj.find_all('p',{'class':'book_tit'})
for title in title_list:
    print(title.text)
