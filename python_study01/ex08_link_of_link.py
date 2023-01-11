import requests
from bs4 import BeautifulSoup

url = "https://www.eosgo.io/"

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")
# print(bs_obj)
news_list = bs_obj.find_all('a',{'class':'news'})
# print(len(news_list))
for news in news_list:
    link = "https://www.eosgo.io/"+news['href']
    # print(link)
    result2 = requests.get(link)
    bs_obj2 = BeautifulSoup(result2.content, "html.parser")
    md = bs_obj2.find('div',{'class','md'})
    print(md.text)
    print("-"*50)


#https://www.eosgo.io/news/this-week-a-stronger-eos-ecosystem