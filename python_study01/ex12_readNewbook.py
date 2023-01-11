#newbook.json파일을 읽어 들여 모든 정보를 출력하도록 합니다.
#완성하면 "1"
import pandas
import json
#
f = open("./Data/newbook.json","r",encoding="utf-8")
data = f.readline()
data = json.loads(data)
# print(data)
book_list = data['book_list']
print(book_list)
print(type(book_list))
# for book in book_list:
#     print(book)

import pandas as pd

# df = pandas.read_json("./Data/newbook.json")
# print(df)











