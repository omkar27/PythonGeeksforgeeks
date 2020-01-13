a = [23,45,654,3,2,34]
mul = 1
for i in a:
    mul = mul*i
print (mul % 57)

for i in range(len(a)):
    a[i] = (a[i-1]+1)%3
print a