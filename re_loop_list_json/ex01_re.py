import re
'''
    이것은 여러줄에 데이터를 표현하기 위한 용도이지만
    주석문으로 사용하기도 합니다.
'''

# a = '''12
# 34
# 56'''
# print(a)

db = '''3412    Bob 123
3834  Jonny 333
4567  Tom   678
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1234  Tiger 123
1548  Kerry 534'''

#r : raw
ns = re.findall(r'[0-9]+', db)
print(ns)

print('-'*50)

#연습) 이름만 출력 해 봅니다.      완성하면 "3"
# names = re.findall(r'[A-z]+',db)
names = re.findall(r'[A-Z][a-z]+',db)
print(names)

#연습) 전화번호만 출력합니다.
#연습) 아이디만 출력합니다.
#                           완성하면 "3"

# phones = re.findall(r'\d{4}',db)
phones = re.findall(r'^\d+',db, re.MULTILINE)
print(phones)

# ids = re.findall(r'\d{3}',db)
ids = re.findall(r'\d+$',db,re.MULTILINE)
print(ids)

#연습) T로 시작하는 이름만 찾아 봅니다.
#연습) T로 시작하지 않는 이름만 찾아 봅니다.
#                                                   완성하면 "3"

tStart = re.findall(r'T[a-z]+',db)
print(tStart)

# notT = re.findall(r'[^T][a-z]+',db) #X
# notT = re.findall(r'[ABCDEFGHIJKLMNOPQRSUVWXYZ][a-z]+',db)
notT = re.findall(r'[A-SU-Z][a-z]+',db)
print(notT)

print(type(notT))
for name in notT:
    print(name)











