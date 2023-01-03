#0에서 9까지의 모든 수를 출력
i = 0
while i<10:
    print(i, end=' ')
    i+=1

print()

for i in range(10):             #종료
    print(i, end=' ')
print()
for i in range(0,10):           #시작,종료
    print(i, end=' ')
print()
for i in range(0,10,1):         #시작,종료,증감
    print(i, end=' ')

print()
#연습) 0~9 숫자를 거꾸로 출력 해 봅니다. (for문 이용)        완성하면 "1"
for i in range(10-1, -1, -1):
    print(i, end=' ')

print()
for i in reversed(range(10)):
    print(i, end=' ')













