class prime:
    def __init__(self,num):
        self.num = num

    def findprime(self):
        isprime = False
        for i in range(2,self.num//2):
           # print "i",i
           # print "num",self.num
           # print "self%num",self.num%i
            if self.num%i == 0:
                isprime = False
            #    print i
            else:
                print i
                isprime = True
        return isprime
pr = prime(9)
print pr.findprime()