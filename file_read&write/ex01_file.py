#  f = open("hello.txt", "w", encoding='utf-8')
# f = open("hello.txt", "a", encoding='utf-8')
# f.write('안녕하세요\n')
# f.write('반갑습니다')
# f.close()
# print('-----파일 생성완료-----')

# 반복문을 사용하여 파일 읽기
# f = open("./Data/out.txt", "w", encoding='utf-8')
# for i in range(1,11):
#     data = "%d번째 줄 입니다.\n" % i
#     f.write(data)
#
# f.close()

# 연습) 2단부터 9단까지 구구단을 파일로 출력
f = open("./Data/gugudan.txt", "w", encoding='utf-8')
for dan in range(2, 10):
    f.write('*** %d단 ***\n' % dan)
    for i in range(1,10):
        r = dan*i
        f.write("%d * %d = %d\n" % (dan,i,r))

f.close()
