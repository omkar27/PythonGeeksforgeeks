def startpyra(num):
    for i in range(num+1):
        for j in range(0,num+1):
            if i>j:
                print "*",
        print ""
    print "*********************"
    for i in range(1,num+1):
        for j in range(1,i+1):
            print j,
        print ""
    print "*********************"
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print i,
        print "",
        print ""
startpyra(5)
