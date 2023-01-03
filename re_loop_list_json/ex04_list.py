# 파이썬에서는 변수를 사용할 때에 자료형을 명시하지 않고 바로 값을 대입합니다.
# 대입한 값에 따라 자료형이 결정됩니다.
#   int   float      str      bool

#   collection:     list    tuple               set      dictionary
#                   []      ()                  {}      {}
#                           리스트의 상수버전


a = [1,3,5,7]
print(a)
print(a[0],a[1],a[2])
print(len(a))

for i in range(len(a)):
    print(i, a[i])

#연습) 리스트를 거꾸로 출력해 봅니다. (2가지)            완성하면 "1"
print()
for i in range(len(a)-1, -1, -1):
    print(i, a[i])
print()
for i in reversed(range(len(a))):
    print(i, a[i])
print()

for i in a:
    print(i, end= ' ')
print()
for i in reversed(a):
    print(i, end=' ')

print()
print(a)
print(reversed(a))
print(list(reversed(a)))
print("-"*50)
a = [1,3,5]
b = (1,3,5)
print(a, type(a))
print(b, type(b))

print(a[0],a[1],a[2])
print(b[0],b[1],b[2])

a[0] = 100
# b[0] = 100          #튜플은 값을 변경시킬 수 없어요!
print(a)
print(b)

a.append(4)
print(a)

# b.append(4)
print("B:", b)
print("-"*50)
a,b  = 3,4
print(a)
print(b)

data = 3,4              #packing
print(data)
i,j = data              #unpacking
print(i, j)

print("-"*50)
a = [1,2,3,4,1,2]
b = (1,2,3,4,1,2)
c = {1,2,3,4,1,2}
print(a, type(a))
print(b, type(b))
print(c, type(c))

b = list(b)
print(b, type(b))
b[0] = 100
print(b)
b = tuple(b)
print(b, type(b))

print('-'*50)
data = [3,5,1,3,5,1,3,5,1,3,5,1]
#연습) 리스트를 유니크하게 만들어 봅니다.                완성하면 "1"

data = list(set(data))
print(data)

print('-'*50)
a = [100,90,80]
b = {'kor':100,'eng':90, 'math':80}
print(b, type(b))

print(a[0])
print(b['kor'])
print(b)
print(b.keys())
print(b.values())
print(b.items())
#연습) keys, values, items를 반복문으로 표현 해 봅니다.       완성하면 "1"
print("-"*50)
for i in b.keys():
    print( b[i])
print('-'*50)
for i in b.values():
    print(i)
print("-"*5)
for i,j in b.items():
    print(i,j)
for i in b.items():
    print(i, i[0], i[1])

print("-"*50)
for i in b:
    print(i, b[i])











