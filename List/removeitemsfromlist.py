a = [2,23,4,6,7,234,34,567,23,6,6,9,4,23,12,1,45,68]

print [i for i in a if i%2==0]

del a[1:15]
print a

b = {2,68}

print [x for x in  a if x not in b]