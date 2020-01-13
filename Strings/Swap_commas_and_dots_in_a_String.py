a = "14, 625, 498.002"
a = a.replace(', ','this')
a = a.replace('.',', ')
a = a.replace('this','.')
print a
print a
li = [23,4,5,6,5,4,3,2,2]

print list(dict.fromkeys(li))