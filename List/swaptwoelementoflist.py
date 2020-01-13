class swap:
    global a
    a =  [1,2,3,4,5,6,7]
    def sw(self,i,j):

        self.i = i
        self.j = j
        an = a[self.i]
        bn = a[self.j]
        a[self.i] = bn
        a[self.j] = an
        return a


s = swap()
print s.sw(1,2)


a = [1,2,3,4,5,6]
def swap(i,j):
    an = a[i]
    bn = a[j]
    a[j] = an
    a[i] = bn
    print a
swap(1,2)
