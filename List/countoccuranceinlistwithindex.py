from collections import Counter
a = [13,43,35,46,34,5,456,45,235,234,35,2]

def countoccure(ind):
    print a.count(a[ind])
    counter = 0
    for i in a:
        if (i == a[ind]):
            counter = counter + 1
    print "Using for loop", counter
    b = Counter(a)
    print "USE COUNTER",b[ind]
    print Counter(a)
countoccure(2)


