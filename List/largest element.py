# program to find largest element from array

mylist = [-1, 1, -1, 8,100]
maxn = mylist[0]
# assign first element to temp
for i in range(len(mylist)):
# iterate through list if max element is present assign max value to temp
    if maxn < mylist[i]:
        maxn = mylist[i]
print maxn
print max(mylist)
print sum(mylist)
