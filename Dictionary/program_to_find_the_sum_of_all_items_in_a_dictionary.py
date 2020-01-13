a = {}
a[1] = 1
a[2] = 2
a[3] = 3

s =0
print a.items()
print list(a.iteritems())
print sum(a.values())
for keys,valu in enumerate(a):
    s = a[valu] + s
print s
su = 0
for i in range(1,len(a)+1):
    su = a[i] + su

print su