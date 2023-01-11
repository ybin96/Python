
import urllib.request
import bs4

url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, 'html.parser')
# print(bs_obj)
title_list = bs_obj.find_all('a', {'class':'cluster_text_headline'})
# print(len(title_list))
for title in title_list:
    print(title.text)