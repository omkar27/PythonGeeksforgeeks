a = "aeiou"

b = []
for i in a:
    if i in 'aeiou':
       # print "Accepted"
        b.append(True)
    else:
        #print "Rejected"
        b.append(False)
#print b

#print all(b)
if all(b) == True:
    print "Accepted"
else:
    print "Rejected"