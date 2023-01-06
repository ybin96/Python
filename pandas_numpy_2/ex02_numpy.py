import numpy
import numpy as np

def pro():
    a = np.arange(5)
    print(a)
    print(list(a))
    print(type(a))
    print(np.arange(10))
    print(np.arange(10,20))
    print(np.arange(10,20,2))
    print(np.arange(5,-5,-1))

    a = np.arange(5)
    print(a.shape, a.ndim, a.dtype)     #(5,) 1 int32

    b = np.arange(6).reshape(2,-1)
    print(b)
    print(b.shape, b.ndim, b.dtype)     #(2, 3) 2 int32

    print(a.size, b.size)
    print(a.itemsize, b.itemsize)
    print(len(a), len(b), len(b[0]))

    print([1,3,5])
    print(np.array([1,3,5]))

    print("-"*50)
    #연습) 0~5까지의 정수가 들어 있는 2행 3열 넘파이 배열을 만들어 봅니다. (3가지)          완성하면 "1"
    print(np.array([[0,1,2],[3,4,5]]))
    print(np.array(range(6)).reshape(2,3))
    print(np.array(range(6)).reshape(2,-1))
    print(np.array(range(6)).reshape(-1,3))
    print(np.array([range(3),range(3,6)]))
    print(np.arange(6).reshape(2,-1))

    print("-"*50)
    #연습) 2차원 배열을 1차원 리스트로 만들어 봅니다.          완성하면 "1"
    a = np.arange(6).reshape(2,3)
    print(a)
    print(list(a))
    b = a.reshape(a.size)
    print(b)

    # b = a.reshape(6)
    # print(b)
    # c = list(b)
    # print(c)


    print("-"*50)

    a = np.array([1,2,3])
    r = a + 10                          #broadcasting           +10을 배열의 원소의 수만큼 합니다.
    print(r)

    b = np.array([4,5,6])               #vector operation       배열의 길이가 같을때에 각 자리의 원소끼리 연산
    r2 = a + b
    print(r2)

    print("-"*50)
    a = np.array([1,2,3])
    b = np.array([4,5,6,7])
    # print(a+b)
    # ValueError: operands could not be broadcast together with shapes (3,) (4,)

#연습) 5개의 변수에 대하여 각각 덧셈을 실시해 봅니다.       어떤것은 연산이 가능하고 어떤것은 연산이 불가능한지 확인합니다.
#                                                    broadcasging? vector operation? 인지 파악합니다.          완성하면 "1"
print("="*50)
a = np.arange(3)                    #(3,) 1 3
b = np.arange(6)                    #(6,) 1 6
c = np.arange(3).reshape(-1,3)      #(1, 3) 2 3
d = np.arange(6).reshape(-1,3)      #(2, 3) 2 6
e = np.arange(3).reshape(3,-1)      #(3, 1) 2 3

#a+b    (3,)+(6,)                   X       1차원배열끼리 원소의 수가 다를 때 연산 불가능
# r1 = a+b
# print(r1)

#a+c    (3,)+(1, 3) ==> (1,3)      O        vector operation을 수행
#2차원배열의 행이 1개짜리이고 2차원 배열의 열의 수가 1차원배열의 원소의 수와 동일할때에 연산이 가능합니다.
# print(a)
# print(c)
# r = a+c
# print(r)
'''
a:[0 1 2]
c:[[0 1 2]]
r:[[0 2 4]]
'''

#a+d    (3,)+(2, 3)  ==> (2, 3)       O         broadcasting
#1차원 배열의 원소와 수와 2차원 배열의 열의 수가 동일하면 연산이 가능하다!
#차원의 배열이 2차원 배열의 행 만큼 연산을 수행합니다.
#(a,) + (n,a)  ==> (n,a) 이런 조건을 만족할 때에 연산이 가능합니다.
# r = a + d
# print(a)
# print(d)
# print(r)
'''
a: [0 1 2]
d: [[0 1 2]
 [3 4 5]]
r:[[0 2 4]
 [3 5 7]]
'''

#a+e    (3,)+(3, 1) ==> (3,3)
# e = np.array([0,1]).reshape(2,-1)
#a+e    (3,)+(2,1) ==> (2,3)
#2차원 배열의 열의 수가 1개 일때는 1차원 배열의 원소의 수 2차원 배열의 행의 수 상관없이 연산이 가능하다.
#(a,) + (b, 1)  ==> (b,a)
# r = a + e
# print(a)
# print(e)
# print(r)
'''
[0 1 2]
[[0]
 [1]
 [2]]
[[0 1 2]
 [1 2 3]
 [2 3 4]]
'''

#b+c    (6,)+(1, 3)         X
#1차원 배열과 2차원이 배열이 연산이 가능한 경우
#       1.  1차원배열의 원소의 수와 2차원 배열의 열의 수가 동일할때    (a,) + (b,a)    ==> (b,a)
#       2.  2차원 배열의 열의 수가 1일때                           (a,) + (b,1)    ==> (b,a)
# r = b + c
# print(r)

#b+d    (6,)+(2, 3)             X
# r = b + d
# print(r)

#b+e    (6,)+(3, 1)     ==> (3,6)
# r = b + e
# print(r)

# c+d    (1, 3)+(2, 3)  ==> (2,3)        broadcasting
# c = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(-1,3)
# c = np.array([1,1,1,1,1,1]).reshape(-1,3)
# 2차원 배열끼리 연산이 가능하려면
#           - 두 배열의 shape가 같으면   vector operation
#           - 두 배열의 shape이 다를 때는 열이 같고 어떤 하나의 배열의  행이 1개이면  broadcasting을 수행합니다.
# r = c+d
# print(c)
# print(d)
# print(r)
'''
c: [[0 1 2]]
d:[[0 1 2]
 [3 4 5]]
r:[[0 2 4]
 [3 5 7]]
'''
#c+e    (1, 3)+(3, 1)  ==> (3,3)
#       행의 수가 1개인 2차원 배열과 열의 수가 1개인 이차원 배열은 연산이 가능하다
#       (1,i) + (j,1)  ==> (j,i)
# c = np.array([1,2,3,4]).reshape(1,-1)
# r = c +e
# print(c)
# print(e)
# print(r)

#d+e    (2, 3)+(3, 1)       X
# e = np.arange(3).reshape(1,-1)
# r = d + e
# print(r)



# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print("-"*50)
# print(a.shape, a.ndim, a.size)
# print(b.shape, b.ndim, b.size)
# print(c.shape, c.ndim, c.size)
# print(d.shape, d.ndim, d.size)
# print(e.shape, e.ndim, e.size)




