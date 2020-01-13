arr = [4,6,8,12]
sum = 0
for i in arr:
    sum = sum+i
print sum

print 'max',max(arr)

print "array rotation", arr[::-1]

for i in range(len(arr)):
    arr[i] = arr[i-1]+1
print arr
