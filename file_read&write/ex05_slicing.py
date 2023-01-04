a = [1,3,5,7,9,0,2,4,6,8]

#특정 위치에 있는 값 하나 갖고 오기   ==> indexing                [숫자]
#어떤 범위에 있는 값들을 갖고 오기    ==> slicing                 [시작:끝]

print(a[0], a[1])
print(a[9], a[len(a)-1], a[-1], a[-2])
print(a[2:5])

#연습) 리스트의 앞쪽 절반을 출력합니다.
#연습) 리스트의 뒤쪽 절반을 출력합니다.             완성하면 "3"
print(a[0:len(a)//2])
print(a[len(a)//2:len(a)])
print(a[:len(a)//2])
print(a[len(a)//2:])
print("-"*50)
print(a[0:-1])
print(a[:])
print(a[0:len(a):1])
print("-"*50)

print(a[1::2])
print(a[::2])

#연습) 거꾸로 출력 해 봅니다.
#연습) 거꾸로 짝수 번째만 출력 해 봅니다.
#연습) 거꾸로 홀수 번째만 출력 해 봅니다.           완성하면 "1"
print(a[-1::-1])
print(a[::-1])
print(a[-1::-2])
print(a[::-2])
print(a[-2::-2])
print("-"*50)
print(a)
print("-"*50)
b = a               #얕은 복사, shallow copy
c = a.copy()        #깊은 복사, deep copy
d = a[:]            #깊은 복사
a[0] = 100
print("a:",a)
print("b:",b)
print("c:",c)
print("d:",d)


