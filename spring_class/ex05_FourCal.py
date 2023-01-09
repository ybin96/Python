class FourCal:
    #파이썬에서는 생성자의 중복을 허용하지 않는다.
    # def __init__(self):
    #     self.first = 4
    #     self.second = 2

    #생성자의 중복은 허용하지 않지만
    #매개변수의 기본값을 주어 같은 효과를 기대 할 수 있어요!
    def __init__(self, first=4, second=2):
        self.first = first
        self.second = second

    def setdata(self,first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return  result

    def mul(self):
        result = self.first * self.second
        return  result

    def div(self):
        result = self.first // self.second
        return  result


# a = FourCal()
# a.setdata(4,2)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())

# a = FourCal()
# b = FourCal()
# a.setdata(4,2)
# b.setdata(3,7)
# print(a.first)
# print(b.first)

# a = FourCal()
# a = FourCal(3,4)
# b = FourCal()               #파이썬에서도 생성자  overloading되는지 확인합니다.       확인하면 "1"
# # a.setdata(3,4)
# print(a.add())
# print(b.add())
# print(a.div())
# print(a.first)
# print(a.second)


class MoreFourCal(FourCal):

    def __init__(self,a,b,c):
        FourCal.__init__(self, a,b)
        self.c = c

    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):
        result = 0
        if self.second != 0:
            result = self.first // self.second
        return result


a = MoreFourCal(4,0,10)
b = MoreFourCal(4,2,10)
# c = FourCal(4,0)
print(a.div())
print(b.div())
# print(c.div())
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())
# print(a.pow())






