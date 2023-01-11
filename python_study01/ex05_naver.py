import bs4
import urllib.request

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")
ul = bs_obj.find('ul',{"class":"list_nav"})
# print(ul)
lis = ul.find_all('li')
# print(lis)
# print(len(lis))
for li in lis:
    a_tag = li.find('a')
    print(a_tag.text)