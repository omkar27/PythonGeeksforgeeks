class sumlist:
    a = []
    def __init__(self,a):
        sum = 0
        self.a = a
        for i in a:
            sum = sum+i
        print sum
if __name__ == '__main__':
    sumlist([2,3,4,5,6,7,8,9])