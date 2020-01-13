#Using for loop

def oddnubn(num):
    print "Omkar"
    for i in range(num):
        if(i%2!=0):
            print i,
    print "**************************************"
    while(num>0):
        if(num%2!=0):
            print num
            num -=1
    print [number for number in [1,2,3,4,5,6,7,89,9,10,11,13,14,5,1111,6] if(number%2!=0)]
    print list(filter(lambda x : (x%2!=0,[1,2,3,4,5,6,7,89,9,10,11,13,14,5,1111,6])))

oddnubn(29)



