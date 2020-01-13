def recbin(a,x):
    start_point = 0
    end_point = len(a)-1
    while start_point <= end_point:
        mid = start_point + (end_point-start_point)//2

        if(a[mid] == x):
            print "Element {} present at index {}".format(x,mid)
            break
        elif a[mid] < x:
            start_point = mid+1
            recbin(a[start_point:end_point],x)
        else:
            end_point = mid-1
            recbin(a[start_point:end_point],x)

lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
x = 10
recbin(lis,x)