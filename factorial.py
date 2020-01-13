class Factorial:
    def __init__(self,num):
        self.num = num
    def fact(self):
        fa = 1
        while(self.num>0):
            fa = fa * self.num
            self.num = self.num-1
        print fa

f = Factorial(5)
f.fact()

