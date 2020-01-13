class Arrayrotate:
    def __init__(self,a):
        self.a = a
        for i in range(1,len(a)+1):
            print a[-i],
        print a[::-1]
if __name__ ==  '__main__':
    Arrayrotate([2,4,56,7,8])

