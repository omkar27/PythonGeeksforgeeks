def bubble(list_a):
    arr_len = len(list_a)
    for i in range(arr_len):
        while list_a[i-1] > list_a[i] and i>0:
            list_a[i-1],list_a[i] = list_a[i],list_a[i-1]
            bubble(list_a)
    return list_a

print bubble([22,3,4,1,3,0,32,42,3,4,45,56,3454,34,2,312,3,43,5,346])