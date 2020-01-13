arr = [3,4,1,2,4,5,2,4]
count = arr.count(arr[0])
for i in range(len(arr)):
    print arr.count(arr[i]),
    if(count<arr.count(arr[i])):
        count = arr.count(arr[i])

print count,
