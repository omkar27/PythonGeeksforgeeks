def eve(num):
    if (num%2 == 0):
        print "if Even"
    else:
        print "if Odd"

    for i in range(1,num):
        if i%2 ==0:
            print "For Even"
        else:
            print "For Odd"
    print [i for i in range(1, num) if i % 2 == 0]
    while(num>0):
        if(num%2==0):
            print "while Even"
        else:
            print "while Odd"
        num=num-1


eve(42)