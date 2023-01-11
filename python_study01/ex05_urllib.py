import urllib.request
import bs4

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
# print(html.read())
bs_obj = bs4.BeautifulSoup(html, "html.parser")
# print(bs_obj)
title = bs_obj.find('a',{'id':'NM_set_home_btn'})
print(title.text)