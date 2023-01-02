# a = int(input('숫자를 입력하세요'))
#
# n = 1
# while n<=a:
#     print('hello')
#     n = n+1

# prompt = '''
# 1. ADD
# 2. DEL
# 3. LIST
# 4. QUIT
# 메뉴를 선택하세요:
# '''
# number = 0
# while number !=4:
#     print(prompt)
#     number = int(input())
#     if number == 1:
#         print('등록')
#     elif number ==2:
#         print('삭제')
#     elif number == 3:
#         print('목록')
#     else:
#         print('종료')

# dan = int(input('구구단'))
# a=1
# while a < 10:
#     print(dan,"*",a,"=",(dan*a))
#     a+=1

# n = int(input('팩토리얼'))
# r=1
# #i=n
# while n>1 :
#     print(n,"*",end='')
#     r *= n
#     n -= 1
# print("1","=",r)

prompt = '''
---선택하시오---
1. 큰수찾기
2. 구구단
3. 종료
'''
# 함수
def max(a, b):
    if a < b:
        return b
    elif a > b:
        return a
    else:
        return "일치"

def gugudan(dan):
    a=1
    while a<10:
        print(dan,"*",a,"=",(dan*a))
        a += 1

number = 0

while number != 3:
    print(prompt)
    number = int(input())
    if number == 1:
        print('------큰수 찾기-------')
        a = int(input('첫번째 숫자'))
        b = int(input('두번째 숫자'))
        c = max(a, b)
        print(c)

        retry = int(input('Y. 다시하기, N. 메뉴로 돌아가기'))
        if retry == 'Y':
            number == 2

    elif number == 2:
        print('------구구단-------')
        dan = int(input('몇단?'))
        print(gugudan(dan))

    else:
        print("종료되었습니다.")
