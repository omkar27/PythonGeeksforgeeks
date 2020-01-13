class Fibo:
    def __init__(self,num):
        self.num = num
    def findfibo(self):
        sum = 0
        for i in range(1,self.num+1):
            sum = sum+i
            print sum

fi = Fibo(10)
fi.findfibo()