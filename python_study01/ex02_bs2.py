import bs4
html_str = '''
    <html>
        <body>
            <ul>
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>
            </ul>
        </body>
    </html>
'''
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
ul = bs_obj.find("ul")
# print(ul)
# li = ul.find("li")
# print(li)
# print(type(li))
# text = li.text
# print(text)
# print(type(text))

lis = ul.find_all('li')
print(lis)
print(type(lis))
print(lis[0])
print(type(lis[0]))
print("-"*50)
for row in lis:
    print(row)
    print(row.text)
    print("-"*50)














