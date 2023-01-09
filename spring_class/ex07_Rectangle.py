class Rectangle:
    def __init__(self,width=0,height=0):
        self.width=width
        self.height=height

    def calcArea(self):
        area = self.width * self.height
        return area

    def setWidth(self,width):
        self.width = width

    def setHeight(self,height):
        self.height = height

a = Rectangle(10,20)
print(a.calcArea())
a.setWidth(20)
a.setHeight(30)
print(a.calcArea())
print(a.width)
print(a.height)
