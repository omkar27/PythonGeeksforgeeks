def insertion(list_a):
    indexing_length = len(list_a)
    for i in range(indexing_length):
        value_to_start = i
        while list_a[i-1] > list_a[i] and i> 0:
            list_a[i],list_a[i-1] = list_a[i-1],list_a[i]
            i = i-1
    return list_a

print insertion([2,78,5,3,2,4,6,7,8,54,3])
