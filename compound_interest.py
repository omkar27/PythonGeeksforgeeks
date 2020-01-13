class Compound:
    def __init__(self,p,r,n,nt):
        self.p = p
        self.r = r
        self.n = n
        self.nt = nt

    def compondinterst(self):
        return (self.p*(1+self.r/self.n)**self.nt)

comp = Compound(28000,5,5,23)
print comp.compondinterst()