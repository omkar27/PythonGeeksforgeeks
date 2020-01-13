class occurance:
    def __init__(self,a,wrd,ind):
        a.self = a
        self.removen(a,wrd,ind)

    def removen(self):
        for i in range(len(self.a)):
            if self.wrd == self.a[i] and  i == self.ind:
                self.a.remove(self.a[i])
        return a

oc = occurance(["hello","hi","hi"],"hi",2)
print oc.removen()
