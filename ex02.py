# a,b=13,4
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
#
# print("-"*50)
#
# a=71
# print(a//10,a%10)
# a = int(input('숫자를 입력하세요'))
# if a %2 == 0:
#     print("짝수")
# else:
#     print('홀수')

# if a>0:
#     print('양수')
# elif a<0:
#     print('음수')
# else:
#     print('제로')
# print('작업종료')

a = int(input('숫자를 입력하세여'))

if 0<a<10:
    print('한자리 숫자')
elif 10<=a<100:
    print('두자리 숫자')
elif 10 <= a < 1000:
    print('세자리 숫자')
else:
    print('네자리 숫자')
