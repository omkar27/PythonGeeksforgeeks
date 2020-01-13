from bisect import bisect_left
a = [2,3,4,3,2,5,6,54]

for i in a:
    if i==4:
        print True
print 6 in a

print 4 in set(a)

so = sorted(a)
print bisect_left(so,90)
