import urllib.request
from bs4 import BeautifulSoup

url = "https://www.hanbit.co.kr/store/books/look.php?p_code=B1068448075"

html = urllib.request.urlopen(url)
bs_obj = BeautifulSoup(html, 'html.parser')
# print(bs_obj)
price = bs_obj.find('span', {'class':'pbr'}).text
book_info = bs_obj.find('div',{'class':'store_product_info_box'})
title = book_info.find('h3').text
info_list = book_info.find('ul',{'class':'info_list'})
span_list = info_list.find_all('span')
writer = span_list[0].text
regdate = span_list[2].text
pages = span_list[3].text
print(title, writer, regdate, pages,price)