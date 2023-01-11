import bs4

html_str = '''
    <html>
        <body>
            <ul class='ko'>
                <li><a href="https://www.naver.com">네이버</a></li>
                <li><a href="https://www.daum.net">다음</a></li>
            </ul>
            <ul class='sns'>
                <li><a href="https://www.google.com">구글</a></li>
                <li><a href="https://www.facebook.com">페이스북</a></li>
            </ul>
        <body>
    </html>
'''

bs_obj  = bs4.BeautifulSoup(html_str, "html.parser")
# atag= bs_obj.find('a')
# print(atag)
# print(atag['href'])

#연습) sns에 있는 모든 a태그의 url를 출력 해 봅니다.     완성하면 "3"
sns = bs_obj.find('ul',{'class':'sns'})
a_list = sns.find_all('a')
for a in a_list:
    url = a['href']
    print(url)