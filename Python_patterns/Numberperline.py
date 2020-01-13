def numperline(num):
    for i in range(num):
        for j in range(1,num+1):
            print j,
        print ""
    print "**********10 9 8 7 6 5 4 3 2 1************"
    for i in range(num):
        for j in range(num,0,-1):
            print j,
        print ""

numperline(10)