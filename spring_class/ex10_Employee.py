class Employee:
    def __init__(self,no,name):
        self.__no = no
        self.__name = name
    def setNo(self,no):
        self.__no = no
    def setName(self,name):
        self.__name=name
    def getNo(self):
        return self.__no
    def getName(self):
        return self.__name
    def computeSalary(self):
        return 0
    def info(self):
        return "사원번호:{},사원이름:{},실수령액:{}".format(self.__no,self.__name,self.computeSalary())
    def __str__(self):
        return "사원번호:{},사원이름:{}".format(self.__no, self.__name)

class SalariedEmployee(Employee):
    def __init__(self,no,name,level):
        Employee.__init__(self, no, name)
        self.__level = level
        self.__base = 0
        self.__sudang = 0
        self.__salary = 0
        self.__salary =  0

    def computeSalary(self):
        if self.__level == 1:
            self.__base = 2000000
            self.__sudang = 200000
        elif self.__level == 2:
            self.__base = 3000000
            self.__sudang = 300000
        else:
            self.__base = 4000000
            self.__sudang = 400000
        self.__salary = self.__base + self.__sudang
        return  self.__salary

    def __str__(self):
        return "{},호봉:{},기본금:{},수당:{},실수령액:{}".format(
            Employee.__str__(self),self.__level, self.__base, self.__sudang, self.__salary)

class HourlyEmployee(Employee):
    def __init__(self,no,name,base,time):
        Employee.__init__(self, no, name)
        self.__base = base
        self.__time = time
        self.__salary  = 0

    def computeSalary(self):
        self.__salary = self.__base * self.__time
        return self.__salary

    def __str__(self):
        return "{},시간당임금:{},일한시간:{},실수령액:{}".format(
            Employee.__str__(self), self.__base,self.__time, self.__salary )


kim = SalariedEmployee(10, "김유신", 1)
lee = HourlyEmployee(20, "이순신", 200000, 15)
hong = SalariedEmployee(30, " 홍길동", 3)
print(kim)
print(lee)
print(hong)
kim.computeSalary()
lee.computeSalary()
hong.computeSalary()
print(kim)
print(lee)
print(hong)

# __str__      함수를 정의하고 객체의 속성값이 출력이 되도록 만들어 봅니다. 완성하면 "3"


#
# # print(kim.getNo(), kim.getName(), kim.computeSalary())
# # print(lee.getNo(), lee.getName(), lee.computeSalary())
# # print(hong.getNo(), hong.getName(), hong.computeSalary())
# print(kim.info())
# print(lee.info())
# print(hong.info())

# data = []
# data.append(SalariedEmployee(10, '김유신', 1))
# data.append(HourlyEmployee(20,'홍길동',200000,15))
# data.append(SalariedEmployee(30, '이신순',3))
#
# for a in data:
#     print(a.info())



