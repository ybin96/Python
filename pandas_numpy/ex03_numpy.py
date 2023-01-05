import numpy as np

a = np.array([4,3,1,5,2])
print(np.max(a))                        #배열중에 가장 큰값을 찾아 줍니다.
print(np.argmax(a))                     #배열중에 가장 큰값이 있는 위치의 인덱스를 반환합니다.
print(a[np.argmax(a)])


# b = np.argsort(a)
# print(a)
# print(b)
# print(a[b])



# a = np.array([3,1,2])
# b = a.argsort()
# print(a)
# print(b)
# print(a[b])



# print(a)
# a.sort()            #배열자신을 정렬해 줍니다. 반환하는 값이 없어요!
# print(a)


# d = [1,3,0,3,1]
# a =  np.zeros([len(d),max(d)+1])
# a[range(len(d)),d] = 1
# print(a)

# d = [1,3,0,3,1]
# '''
#   위의 일차원 배열의 원소의 수 만큼 행을 갖는 2차원 배열을 만들고 각 값의 자리에 1을 설정하는 배열을 만들어 보세요.  완성하면 "3"
#   0 1 0 0
#   0 0 0 1
#   1 0 0 0
#   0 0 0 1
#   0 1 0 0
# '''
# a =  np.zeros([len(d),max(d)+1])
# # a[0][1] = 1
# # a[1][3] = 1
# # a[2][0] = 1
# # a[3][3] = 1
# # a[4][1] = 1
# a[range(5),d] = 1
# print(a)



# #연습) 5*5 배열을 대각선으로만 1로 채웁니다.        완성하면 3
# a = np.zeros([5,5])
# # a[[0,1,2,3,4],[0,1,2,3,4]] = 1
# a[range(5),range(5)]= 1
# print(a)

#연습) 테두리가 1로 채워지고 속은 0으로 채워진 5*5 배열을 만들어 봅니다.       완성하면 "1"
# a = np.zeros([5,5])
# # a[0] = 1
# # a[-1] = 1
# a[[0,-1]] = 1
# a[:,[0,-1]] = 1
# print(a)
#
# b = np.ones([5,5])
# b[1:-1, 1:-1] = 0
# print(b)



# a = np.arange(20).reshape(-1, 4)
# print(a)
# a[:] = -1
# a[0] = 9
# print(a)




# a = np.arange(20).reshape(-1, 4)
# print(a)
# #        행행행   열열열
# print(a[[1,3,4],[0,2,3]])       #(1,0), (3,2), (4,3)



# print(a[a>5])               #bool array
# # [ 6  7  8  9 10 11 12 13 14 15 16 17 18 19]
# print(a[[1,3]])             #index array
# # [[ 4  5  6  7]
# #  [12 13 14 15]]
# print(a[[3,1]])



# print(a[1])             #1행을 갖고 옵니다.
# print(a[1,2])           #1행 2열의 원소 한개를 갖고 옵니다.          ==> 값 한개
# print(a[[1,3]])         #1행과 3행을 갖고 옵니다.                   ==> 2차원 배열



def not_used16():
    a = np.arange(12).reshape(-1, 4)
    print(a)
    # a[:] = -1
    # a[:,0] = 9

    b = a>5
    print(b)

    c = a[b]
    print(c)

    d = a[a>5]           #bool array
    print(d)


def not_used15():
    a = np.arange(12).reshape(-1, 4)
    print(a)
    #연습) for문을 이용하여 다음과 같이 행과 열을 바꿔서 출력 해 봅니다.          완성하면 "1"
    # 0 4 8
    # 1 5 9
    # 2 6 10
    # 3 7 11

    # print(a[:,0])
    # print(a[:,1])
    # print(a[:,2])
    # print(a[:,3])
    #
    # print(len(a[0]))

    # for i in range(len(a[-1])):
    #     print(a[:,i])

    # for i in range(a.shape[-1]):
    #     print(a[:,i])

    print(a.transpose())        #행과 열을 바꿔주는 함수입니다.




    # print(a[::-1][::-1])        #행을 거꾸로 했다가 다시 행을 거구로 ==> 그래서 원래가 됩니다.
    # #연습) 행도 거꾸로 열도 거꾸로 출력 해 봅니다.
    # print(a[::-1,::-1])


    # print(a[::-1])
    # print(a[0,0])
    #
    # #아래의 결과는 동일한 원소이지만 차원이 달라요!
    # print(a[:2,0])
    # print(a[:2,:1])
    # # [0 4]
    # # [[0]
    # #  [4]]
    # print(a[:2,:2])
    # print(a[:,-1])





def not_used14():
    a = np.arange(12).reshape(-1, 4)
    print(a)
    # b = a[0][0]
    # c = a[0,0]                              # fancy indexing
    # print(b)
    # print(c)
    # d = a[:,1]
    # print(d)
    #
    # #표시한 요소만 갖고 오도록 해 봅니다.      완성하면 "3"
    # e = a[1:,1:3]                            # 2차원의 결과가 됩니다.          열에 대하여 슬라이싱을 하려면 팬시인덱싱으로 표현해야 합니다.
    # print(e)



def not_used13():
    a = np.arange(20).reshape(-1, 4)
    print(a)

    # b = a[1][2]                           #2차원 배열에서의 인덱싱
    # b =  a[0][0]                          #2차원 배열에서의 맨 첫번째 요소
    # b = a[-1][-1]                         #2차원 배열에서 맨 마지막 요소
    # b = a[0]                              #2차원배열의 0번째 행을 갖고 옵니다.          1차원배열을 갖고 옵니다.
    # b = a[1:3]                            #1번째 행부터 2번째 행까지 슬라이싱          2차원배열을 갖고 옵니다.
    # b = a[3:]                               #3번째 행부터 끝까지 슬라이싱                2차원배열을 갖고 옵니다.
    b = a[::-1]
    print(b)
    print(type(b))
    #연습) 행을 거꾸로 출력 해 봅니다.       완성하면 "3"

def not_used12():
    a = np.arange(12)
    print(a)
    # a[0] = -1                             #인덱싱으로 값을 바꾸기
    # a[:3]  = -1                           #슬라이싱으로 값을 바꾸기
    # a[:] = -1                             #전부다 바꾸기
    a[1::2] = -1                            #홀수번째만 바꾸기
    print(a)

def not_used11():
    a = np.arange(12)
    print(a)
    b = a[0]                #특정 자리의 값 하나 갖고 오기      indexing
    print(b)
    print(type(b))

    c = a[0:3]             #특정 범위의 값들을 갖고 오기        slicing     반환하느것은 넘파이배열
    print(c)
    print(type(c))

    d = a[:3]              #맨처음 요소부터 갖고 올때는 생략할 수 있어요
    print(d)

    e = a[5:]             #맨마지막도 생략할 수 있어요
    print(e)

    f = a[:]            #시작도 생략, 끝도 생략하면 전부다
    print(f)

    g = a[::-1]         #거꾸로 뒤집어서 갖고 와요
    print(g)

    h = a[::2]          #짝수번째만 슬라이싱
    print(h)

    i = a[1::2]         #홀수번재만 슬라이싱
    print(i)

def not_used10():
    a = np.arange(12).reshape(3,-1)
    print(a)

    #a배열과 동일한 shape의 0으로 채워진 배열을 만들어요
    b = np.zeros_like(a)
    print(b)

    #a배열과 동일한 shape의 1으로 채워진 배열을 만들어요
    c = np.ones_like(a)
    print(c)

    #a배열과 동일한 shape의 100으로 채워진 배열을 만들어요
    d = np.full_like(a, 100)
    print(d)

def not_used9():
    a = np.arange(12).reshape(3,-1)
    print(a)
    b = np.cumsum(a, axis=0)       #배열의 원소들을 수직으로 누적하여 합을 만들어 줍니다.      2차원배열 생성
    c = np.cumsum(a, axis=1)       #배열의 원소들을 수평으로 누적하여 합을 만들어 줍니다.      2차원배열 생성
    d = np.cumsum(a)               #모든 배열의 원소들을 차례로 누적한                     1차원배열 생성
    e = d.reshape(-1,4)            #필요하다면 차수를 바꾸어 줍니다.
    print(b)
    print(c)
    print(d)
    print(e)



def not_used8():
    a = np.arange(12).reshape(3,-1)
    print(a)
    max = np.max(a)                 #전체요소중에 제일 큰값
    max0 = np.max(a, axis=0)        #수직으로 제일 큰값
    max1 = np.max(a, axis=1)        #수평으로 제일 큰값
    print(max)
    print(max0)
    print(max1)

def not_used7():
    a = np.arange(12).reshape(3,-1)
    print(a)

    sum = np.sum(a)             #배열의 모든 원소를 더하기 해 줍니다.ㄴ
    sum0 = np.sum(a,axis=0)     #수직     열의 수와 동일한 1차원 배열이 만들어 져요
    sum1 = np.sum(a,axis=1)     #수평     행의 수와 동일한 1차원 배열이 만들어 져요.
    print(sum)
    print(sum0)
    print(sum1)


def not_used6():
    a = [10,20,30,40,50]
    b = np.array(a)
    tot = np.sum(b)
    print(tot)
    tot2 = np.sum(a)  #넘파이 배열이 아닌것도 처리 해 줍니다.
    print(tot2)





def not_used5():
    a = np.arange(12)
    print(a)

    #배열의 차원을 바꾸기 위하여 reshape함수를 이용합니다.
    b = a.reshape(3,4)
    print(b)

    #넘파이배열의 차원을 확인 할 때에 shape을 이용합니다.
    print(a.shape)  #(12,)
    print(b.shape)  #(3, 4)

    #열의 수만 지정하고 행의 수는 알아서 해줘 -1
    c = a.reshape(-1,4)
    print(c)

    d = a.reshape(2,-1)
    print(d)

    e = a.reshape(5,-1)         #오류
    print(e)
    #ValueError: cannot reshape array of size 12 into shape (5,newaxis)
    #12까리 1차원배열을 5행짜리 2차원 배열로 만들 수 없어요
    #원소에 개수에 맞추어 차원을 바꿔야 합니다.




def not_used4():
    #0부터 12-1까지 1씩증가한 요소를 갖는 1차원 배열을 만들어 줍니다.
    a  = np.arange(12)
    print(a)

    b = np.arange(1,11,1)
    print(b)

    c = np.arange(0,1,0.1)
    print(c)

    d = np.arange(10,0,-1)
    print(d)


def not_used3():
    #1로 채워진 배열을 만들어요
    a = np.ones(3)
    print(a)

    #연습) 3행 4열의 1로 채워진 데이터의 자료형이 정수인 배열을 만들어 봅니다.
    b = np.ones([3,4], dtype=np.int32)
    print(b)

    #특정값으로 채워진 배열을 만들 때에 full(크기,값)
    c = np.full(3,2)
    print(c)

    d = np.full(3,2.0)
    print(d)



def not_used2():

    #0으로 채워진 3개짜리의 배열을 만들어 줍니다.
    #배열의 요소가 "실수"입니다.
    a= np.zeros(3)
    print(a)

    #데이터요소의 자료형이 정수인 배열을 만들어 줍니다.
    b = np.zeros(3, dtype=np.int32)
    print(b)


    #0으로 채워진 3행 4열의 2차원 배열을 만들어요
    c = np.zeros([3,4])
    print(c)

    #0으로 채워진 데이터의 자료형이 정수인 3행 4열의 2차원 배열을 만들어요
    d = np.zeros([3,4], dtype=np.int32)
    print(d)







def not_used():
    a = [10,20,30,40]
    b = np.array(a)
    c = np.arange(10,50,10)
    # d = np.arange([10,20,30,40]) #오류
    print(a)
    print(b)
    print(c)
    # print(d)