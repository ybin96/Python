class A:
    def __init__(self,a):
        self.a = a

class B(A):
    def __init__(self,a,b):
        A.__init__(self, a)
        self.b = b

data = B(3,4)
print(data.a, data.b)