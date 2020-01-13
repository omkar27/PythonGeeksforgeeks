def printalpha():
    print "************A A A A A*****************"
    for i in "ABCDE":
        for j in "ABCDE":
            print i,
        print ""
    print "************A B C D E*****************"
    for i in "ABCDE":
        for j in "ABCDE":
            print j,
        print ""
    print "**************EEEEEEE Reverse*******************"
    for i in "EDCBA":
        for j in "ABCDE":
            print i,
        print ""
    print "**************EDCBA Reverse*******************"
    for i in "EDCBA":
        for j in "EDCBA":
            print j,
        print ""
printalpha()