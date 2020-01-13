class ith:
    def __init__(self,st,ind):
        self.st = st
        self.ind = ind

    def removeith(self):
        print self.st[:self.ind]

if __name__ == '__main__':
    a = "Omkar"
    i = ith(a,4)
    i.removeith()
