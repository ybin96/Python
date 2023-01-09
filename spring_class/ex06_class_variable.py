class Family:
    lastname = "김"
    def __init__(self, firstname):
        self.firstname=firstname

    def info(self):
        print(self.firstname, self.lastname)

print(Family.lastname)
# print(Family.firstname)
a = Family('철수')
b = Family('철민')
a.info()
b.info()
Family.lastname = "박"
a.info()
b.info()
print(a.lastname)
print(b.lastname)
print(Family.lastname)
print("-"*50)
'''
    객체를 통해서도 클래스변수를 사용할 수 있어요.
    그런데 객체를 통해 클래스변수를 변경할 때에는 그 객체에만 해당이 되고 
    클래스변수에는 영향을 끼치지 않아요!
'''
a.lastname = "홍"
print(a.lastname)
print(b.lastname)
print(Family.lastname)
