import json
data = '{"ip":"8.8.8.8"}'
print(data, type(data))

d1 = json.loads(data)
print(d1, type(d1))

d2 = json.dumps(d1)
print(d2, type(d2))

print("-"*50)

import requests
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
text  = requests.get(url).text
text = bytes(text, 'iso-8859-1').decode('utf-8')
print(text)
print(type(text))

#연습) 모든 도시코드와 도서이름을 출력합니다.          완성하면 "3"







