class simpleinterest():
    def __init__(self,p,r,t):
        self.p = p
        self.r = r
        self.t = t

    def simple(self):
        return (self.p+self.r+self.t)/100

simp = simpleinterest(1360000,7,5)
print simp.simple()
