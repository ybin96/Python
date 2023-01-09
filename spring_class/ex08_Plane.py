class Plane:

    planes = 0

    def __init__(self,maker="보잉",model="보잉747",seats=300):
        self.__maker = maker
        self.__model = model
        self.__seats = seats
        Plane.planes += 1

    def setMaker(self, maker):
        self.__maker = maker

    def setModel(self,model):
        self.__model = model

    def setSeats(self,seats):
        self.__seats = seats

    def getMaker(self):
        return self.__maker

    def getModel(self):
        return self.__model

    def getSeats(self):
        return self.__seats

    def getPlanes(self):
        return Plane.planes

print('비행기 대수 {}'.format(Plane.planes))

a = Plane('에어버스','A380',500)
b = Plane()
# print(a.maker,a.model,a.seats)
# a.seats=400
# print(a.maker,a.model,a.seats)
print(a.getMaker(), a.getModel(), a.getSeats())
a.setSeats(400)
print(a.getMaker(), a.getModel(), a.getSeats())
print(b.getMaker(), b.getModel(), b.getSeats())
print('비행기 대수 {}'.format(Plane.planes))
print('비행기 대수 {}'.format(a.getPlanes()))