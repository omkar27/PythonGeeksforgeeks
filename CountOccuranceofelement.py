arr = [2,5,67,3,5,567,3,5,576,3,23,65,67,8,3]

a= 67
count = 0
for i in arr:
    if (i==a):
        count +=1
#print count


# for i in range(len(arr)):
#     print "Index",i
#     min  = arr[i]
#     if (min < arr[i+1]):
#         min = min
#     else:
#         min = arr[i+1]
# print "MIN",min

alist = [-32,43,43,5,34,23,23,4,-54,-12,-98]
neg = 0
pos = 0
for i in alist:
    if(i<0):
        print "-VE",i
        neg += 1
    else:
        print "+VE",i
        pos += 1
print "-VE count",neg
print "+VE count",pos

alist.remove(-32)
print alist

tuplarray = [(234,42),(2,4,5),(12,32),(455,34,23),(4,7,36,67)]
for index,i in enumerate(tuplarray):
    if len(i) == 0:
        print "Index",index
        print "Empty tuple",i
    else:
        print "No empty tuple"