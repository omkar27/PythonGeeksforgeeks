pi = 3.14
class Circle:
    def __init__(self,r):
        self.r = r

    def Area(self):
        return pi*pow(self.r,2)

cir = Circle(45)
print cir.Area()