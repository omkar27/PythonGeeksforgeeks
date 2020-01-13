def firstthreeodd(x):
    su = 0
    cntr = 0
    for i in range(len(x)):
        if x[i]%2 != 0 and cntr<3:
            su = su+x[i]
            cntr +=1
    print su

a = [0,1,2,3,4,5,6,7,8,9,10]
firstthreeodd(a)